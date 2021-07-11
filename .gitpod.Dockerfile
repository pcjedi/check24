# FROM gitpod/workspace-full

from python:3.9

RUN python -m venv /opt/venv1
RUN /opt/venv1/bin/pip install requests

ENV WORKON_HOME /opt
