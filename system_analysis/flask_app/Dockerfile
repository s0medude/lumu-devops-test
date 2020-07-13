
# For matter of security the command ADD shoulb be replace by COPY
FROM alpine
# The port 9000 must be exposed in the container to communicate to the outside world
EXPOSE 9000
RUN apk add py3-pip build-base python3-dev libffi-dev openssl-dev
RUN mkdir -p /opt/api
WORKDIR /opt/api
COPY api/requirements.txt /opt/api
# It is a better practice to include virtualenv  to insolote the python application
# from the other python files in the system 
RUN pip3 install virtualenv && python3 -m venv venv
RUN pip3 install --no-cache-dir -r requirements.txt
COPY api/. /opt/api
