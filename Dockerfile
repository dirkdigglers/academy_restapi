# See https://docs.docker.com/engine/reference/builder/#format
#     https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/
#
# Basics
#
FROM alpine:latest

LABEL maintainer="thomas.wetzler@t-systems.com"

# Install Python 3 to Alpine
RUN apk add --no-cache curl && \
    apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache

# Install Flask
RUN pip3 install flask connexion configparser flask_cors requests

# Setup Environment 
COPY src/ /srv/ 
RUN  chmod u+x /srv/server.py
RUN  chmod u+x /srv/test.py; cd /srv

# Start Server
WORKDIR /srv
#ENTRYPOINT /srv/server.py
ENTRYPOINT /bin/sh

 
