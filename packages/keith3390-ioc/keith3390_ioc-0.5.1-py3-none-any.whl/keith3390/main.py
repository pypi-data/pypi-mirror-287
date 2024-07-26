#!/usr/bin/python3

from emmi_escpi.application import Application
from emmi.scpi import MagicScpi

import logging, asyncio, os, sys, time

logger = logging.getLogger("keith3390-ioc")        

def main(args=None, env=None):
    if args is None:
        args = sys.argv.copy()
    if env is None:
        env = os.environ.copy()

    app = Application(args=args, env=env)
    app.setupIoc(env_prefix_map={'KEITH3390': None})
    app.runIoc()

if __name__ == "__main__":
    main()
