# FROM gitpod/workspace-full

from python:3.9

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    git \
    openssh-client \
    sudo \
    vim \
    wget \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
 
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers


RUN python -m venv /opt/venv1 && \
    /opt/venv1/bin/pip install requests

RUN python -m venv /opt/venv2 && \
    /opt/venv2/bin/pip install tqdm
    
ENV WORKON_HOME /opt
