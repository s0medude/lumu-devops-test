# lumu-devops-test

DevOps Engineer Technical Test - Lumu Technologies

### System Analysis

- We are running a Python Flask application using ​gunicorn​ and ​nginx​ in adockerized container. This is how our deployment files look like:

    - [Dockerfile](./Dockerfile)
    - [docker-entrypoint](./docker-entrypoint.sh)
    - [nginx.conf](./nginx.conf) 

    - Most of the time the service is running without problems. However, we arefacing situations where the flask application stops working or fails, yet thedocker container keeps running making it difficult to detect when it happens.Additionally, when running as a standalone application, the flask applicationlogs its activity and errors to the standard output, but in production we arenot able to see the log.

    - Please highlight any problem you can spot (if any) in those files. Thendiagnose the problem we are facing and propose a working solution.

    - Note: The actual Python code is irrelevant for our purposes, it could be anyarbitrary Flask application.
