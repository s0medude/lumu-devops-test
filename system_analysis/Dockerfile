
# OLD DOCKERFILE

FROM alpine
RUN apk add py3-pip build-base python3-dev libffi-dev openssl-dev
RUN apk add nginx
RUN mkdir -p /opt/api
WORKDIR /opt/api
ADD api/requirements.txt /opt/api
RUN pip3 install --no-cache-dir -r requirements.txt
ADD api/. /opt/api
ADD ./docker-entrypoint /bin/docker-entrypoint
ADD ./nginx.conf /etc/nginx/nginx.conf
CMD [​"/bin/docker-entrypoint"​]

# For a matter of security the command ADD shoulb be replace by COPY

FROM alpine
RUN apk add py3-pip build-base python3-dev libffi-dev openssl-dev
RUN apk add nginx
RUN mkdir -p /opt/api
WORKDIR /opt/api
COPY api/requirements.txt /opt/api
RUN pip3 install --no-cache-dir -r requirements.txt
COPY api/. /opt/api
COPY ./docker-entrypoint /bin/docker-entrypoint
COPY ./nginx.conf /etc/nginx/nginx.conf
CMD [​"/bin/docker-entrypoint"​]
