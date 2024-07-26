FROM python:3.12

USER root

RUN mkdir -p /etc/keith3390
COPY keithley-3390.yml visa-sim-keith3390.yml /etc/keith3390

ARG KEITH3390_SRC=/keith3390_src
ARG KEITH3390_FROM_PIP=yes

RUN useradd -u 9999 cthulhu && mkdir /home/cthulhu && chown cthulhu /home/cthulhu

RUN if [ -d "$KEITH3390_SRC" ]; then \
        echo "Installing from local directory: $KEITH3390_SRC" ;\
        pip install "$KEITH3390_SRC"[test] ;\
    elif [ "$KEITH3390_FROM_PIP" = "yes" ]; then \
        echo "Installing from pip" ;\
        pip install keith3390[test] ;\
    else \
        echo "\n  ***\n  *** Source not found at \$KEITH3390_SRC ($KEITH3390_SRC) -- failing build now. \n  ***\n" ;\
        /bin/false ;\
    fi


USER cthulhu

ENTRYPOINT [ "keith3390-ioc", "--from-yaml", "/etc/keith3390/keithley-3390.yml" ]

