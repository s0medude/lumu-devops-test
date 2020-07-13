# lumu-devops-test

DevOps Engineer Technical Test - Lumu Technologies

### System Analysis

- We are running a Python Flask application using ​gunicorn​ and ​nginx​ in adockerized container.

    - Most of the time the service is running without problems. However, we arefacing situations where the flask application stops working or fails, yet the docker container keeps running making it difficult to detect when it happens. Additionally, when running as a standalone application, the flask application logs its activity and errors to the standard output, but in production we are not able to see the log.

    - Please highlight any problem you can spot (if any) in those files. Then diagnose the problem we are facing and propose a working solution.

    - Note: The actual Python code is irrelevant for our purposes, it could be any arbitrary Flask application.


    #### Estrategies

    - I will split the initial Docker container in two containers for a better manipulation and troubleshooting because we insolate each oneof those and can hadle independently. In each we import the respectly image, copies our files, and replaces them with default ones.
        - [Flask Dockerfile](./flask_app/Dockerfile)
        - [Nginx Dockerfile](./nginx/Dockerfile) 

    - The fisrt part of the *nginx.conf* contains all fundamental Nginx info and variables. I'm notice that the proxy configuration was a quite wrong, so there are several things to note:
        - [nginx.conf](./nginx/nginx.conf)

        1. Take a look at server_name for a better understanding of what are we doing
        2. Take a look at listen 80. That command specifies what port the app will run at.
        3. And last but not least, proxy pass command that should point Nginx configuration to the flask project.

    - I decided to deploy our application and proxy server together with docker-compose to make them talk to each other and run the whole system.        

        - [Docker Compose](./docker-compose.yml)
        - The docker compose is split in to parts *flask_app* and *nginx*. The *flask_app* container executes Gunicorn that runs the Flask app and translates it to 9000 port with 16 worker in a virtualenv for better insolation. And the second container just runs Nginx on 80 port.

    - Finally the following script runs docker-compose

        - [docker-entrypoint](./docker-entrypoint.sh)   


    - For the logs problem check to see if our Flask application is being run directly or through Gunicorn, and then set your Flask application logger’s handlers to the same as Gunicorn’s. And then finally, have a single logging level between Gunicorn and the Flask application.