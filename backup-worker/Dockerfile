FROM ubuntu:20.04


RUN apt-get update && \
    apt-get install -y wget gnupg build-essential curl python3-pillow python3-dev python3-numpy python3-pip && \ 
    rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --no-cache-dir requests dateutils


RUN cd /tmp && curl -L --output overviewer.tgz https://github.com/overviewer/Minecraft-Overviewer/tarball/master && \
    tar xzf overviewer.tgz && rm overviewer.tgz && \
    cd overviewer* && \
    python3 setup.py build && \
    python3 setup.py install && \
    cd .. && rm -rf overviewer*
    

COPY . /work

WORKDIR /work

ENTRYPOINT ["/work/run.sh"]

