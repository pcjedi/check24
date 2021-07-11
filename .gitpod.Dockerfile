# FROM gitpod/workspace-full

from python:3.9

RUN python -m venv /opt/venv1 && \
    /opt/venv1/bin/pip install requests

RUN python -m venv /opt/venv2 && \
    /opt/venv2/bin/pip install tqdm
    
ENV WORKON_HOME /opt
