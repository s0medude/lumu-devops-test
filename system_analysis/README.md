# lumu-devops-test

DevOps Engineer Technical Test - Lumu Technologies

### System Analysis

- We are running a Python Flask application using ​gunicorn​ and ​nginx​ in adockerized container. This is how our deployment files look like:

    - Dockerfile

    `FROM alpineRUN apk add py3-pip build-base python3-dev libffi-dev openssl-dev`
    `RUN apk add nginx`
    `RUN mkdir -p /opt/api`
    `WORKDIR /opt/api`
    `ADD api/requirements.txt /opt/api`
    `RUN pip3 install --no-cache-dir -r requirements.txt`
    `ADD api/. /opt/apiADD ./docker-entrypoint /bin/docker-entrypoint`
    `ADD ./nginx.conf /etc/nginx/nginx.conf`
    `CMD [​"/bin/docker-entrypoint"​]`

    - docker-entrypoint

    `#!/bin/ash`

    `echo​​"Starting gunicorn..."gunicorn -w 16 -b 127.0.0.1:9000 app:app --daemon`
    `sleep 3`
    `echo​​"Starting web server..."`
    `nginx -g ​"daemon off;`

    - nginx.conf

    `user nginx;`
    `worker_processes auto;`
    `pid /tmp/nginx.pid;pcre_jit on;`
    `error_log /var/​log​/nginx/error.log warn;`
    `events {  ` 
        `worker_connections  1024;`
    `}`
    `http {  ` 
        `include /etc/nginx/mime.types;   `
        `default_type text/json;   `
        `server_tokens off;   `
        `client_max_body_size 0;   `
        `log_format  main  ​'$remote_addr - $remote_user [$time_local] "$request" `
                            `'​'$status $body_bytes_sent "$http_referer" '`
                            ​`'"$http_user_agent" "$http_x_forwarded_for"'​;`
        `access_log /var/​log​/nginx/access.log  main;   `
        `sendfile       on;   `
        `tcp_nopush     on;   `
        `tcp_nodelay    on;   `
        `keepalive_timeout  65;   `
        `
        `server` `{`      
            `listen 9180;`
            `charset utf-8;`
            `location` `/` `{ `          
                `proxy_pass http://localhost:9000;`       
           `}`   
       `}`
    `}`