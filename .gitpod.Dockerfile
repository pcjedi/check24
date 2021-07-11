# FROM gitpod/workspace-full

FROM python:3.9

RUN apt-get update \
 && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    git \
    openssh-client \
    sudo \
    vim \
    wget \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
 
RUN echo '%gitpod ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

ENV WORKON_HOME /opt

RUN python -m venv $WORKON_HOME/venv1 && \
    $WORKON_HOME/venv1/bin/pip install requests

RUN python -m venv $WORKON_HOME/venv2 && \
    $WORKON_HOME/venv2/bin/pip install tqdm
    
