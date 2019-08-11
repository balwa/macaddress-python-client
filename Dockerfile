FROM python:3.7-alpine
LABEL git_repo=https://github.com/balwa/macaddress-python-client

COPY mac_vendor.py /tmp/mac_vendor/
COPY docker_helper.sh /tmp/docker_helper.sh

ARG MACADDRESSIO_API_KEY
ENV MACADDRESSIO_API_KEY ${MACADDRESSIO_API_KEY}

ENV PATH $PATH:/tmp/mac_vendor/

WORKDIR /tmp/mac_vendor/
CMD [ "/bin/sh", "/tmp/docker_helper.sh" ]