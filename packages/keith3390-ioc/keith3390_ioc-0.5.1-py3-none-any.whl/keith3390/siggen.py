from emmi.scpi import MagicScpi

import logging, asyncio, os, sys, time

logger = logging.getLogger(__name__)

import numpy as np
import scipy.signal as sig

class SignalGenerator:
    def __init__(self, ufunc_size=65536, **scpi_kwargs):
        self.scpi = MagicScpi(**scpi_kwargs)
        args = [ f'{k}="v"' for k,v in scpi_kwargs.items() ]
        logger.info(f'io={self.scpi} {" ".join(args)}')

        self._user_func = np.zeros(ufunc_size)


    @property
    def ufunc(self):
        # Access to a "volatile function", i.e. user-defined trace.
        return self._user_func


    @ufunc.setter
    def ufunc(self, val):
        if len(val) != len(self._user_func):
            logger.warning(f'desc="Resampling necessary"  '
                           f'received={len(val)} required={len(self._user_func)}')
            v = sig.resample(val, len(self._user_func))
        else:
            v = val
        self._user_func[:] = v[:]
        self.scpi.DATA.DAC("VOLATILE", *(self._user_func))
        self.scpi.FUNC.USER("VOLATILE")
        self.scpi.FUNC("USER")

        
    def _is_builtin_func(self, fname):
        for i in ("sinus", "squ", "ramp", "puls", "noise", "dc"):
            if fname.lower().startswith(i):
                return True
        return False

    @property
    def func(self):
        # A little more advanced access to scpi.FUNC.
        # For the Keithley 3390, there are the following "built-in functions":
        # SIN, SQU, RAMP, PUL, NOIS, DC, USER. These are set by "FUNC {name}"
        # Everything else is set by "FUNC USER", followed by "FUNC:USER {name}",
        # where there are other names, one of them being VOLATILE (for the
        # volatile user-defined function -- see above).
        fname = self.scpi.FUNC()
        if fname.lower() != "user":
            return fname

        return self.scpi.FUNC.USER()


    @func.setter
    def func(self, fname):
        try:
            if self._is_builtin_func(fname):
                logger.info(f'desc="Built-in function" fname="{fname}"')
                self.scpi.FUNC(f"{fname}")
                return
            else:
                cat = self.scpi.DATA.CAT()
                for c in [r.strip('"') for r in cat]:
                    if c.lower().startswith(fname.lower()):
                        logger.info(f'desc="USER-catalog function" fname="{fname}"')
                        self.scpi.FUNC("USER")
                        self.scpi.FUNC.USER(fname)
                        return
                logger.error(f'desc="Cannot set USER function" fname={fname}')
        except Exception as e:
            logger.error(f'error="{str(e)}" fname="{fname}"')
        logger.error(f'desc="Cannot set function" fname="{fname}"')
            
