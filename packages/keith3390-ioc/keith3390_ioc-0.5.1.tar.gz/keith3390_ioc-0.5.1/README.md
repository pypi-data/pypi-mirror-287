EPICS IOC for the Keithley 3390 Signal Generator
================================================

This is a quick'n dirty IOC based on the experimental magic-IOC application
[`escpi`](https://gitlab.com/codedump2/escpi), part of the
[EMMI](https://gitlab.com/codedump2/emmi) ecosystem.

Essentially, here we're just bundling a Dockerfile, configuration, and
some documentation for the IOC.

Versioning follows roughly the versioning of `escpi`.

Quick Start
-----------

The easiest way is to run the `keith3390-ioc` directly from its official
Podman container:
```
$ podman run -ti --rm registry.gitlab.com/kmc3-xpp/keith3390-ioc --prefix KEITH:
```

Enviroment Variables and Parameters
-----------------------------------

Being essentially just a deployment of `escpi`, Keith-3390 responds to the
same environment variables and parameters:

- `--prefix` the EPICS prefix to use
- `--resource-manager` the PyVISA resource manager to use (defaults to `"@py"`)
- `--device` the PyVISA device to connect to

EPICS Process Variables
-----------------------

Exports the following EPICS PVs (`{prefix}` is as specified in the command
line parameters):

- `{prefix}:func` the waveform to generate, must be one of "SIN", "DC", "NOISE",
  "SQUA", "RAMP", "USER".
- `{prefix}:func_RBV` the currently used wave form
- `{prefix}:freq` the frequency with which to generate the waveform, in Hz
- `{prefix}:freq_RBV` read back value of the current frequency
- `{prefix}:ampl` the amplitude to apply to the signal
- `{prefix}:ampl_RBV` read back value of the amplitude
- `{prefix}:offs` the signal offset (i.e. base voltage value)
- `{prefix}:offs_RBV` read back value of the offset
- `{prefix}:onoff` if a 1 is written here, the Keithley's output
   is turned ON (i.e. the function is being provided). If this is set to
   0, the output is muted.

