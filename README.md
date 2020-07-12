# lumu-devops-test

DevOps Engineer Technical Test - Lumu Technologies

### General Questions 

1. You will be in charge of running a set of JVM-based microservices connected to MongoDB, exchanging messages through a kafka broker and communicating with external clients using HTTP Restful Services.

- What metrics do you consider the most critical to monitor for the system and what tools would you use?

    ##### Answer

    In my opinion, the first thing to consider it is to have uniformity in types of metrics being collected across all microservices and the consistency of metrics across multiple microservices. This make easier the reusability, reability and make dashboards intuitive even with hundrends of microservices. Also if it is a cloud-architecture, monitoring cloud usage costs, and monitor different cloud services should be consider too.

    ###### Commonly collected metrics relevant to microservices:

    **Resource utilization metrics**

    - Resource utilization metrics (CPU, threads, file descriptors, JVM heap, and garbage collection metrics)
    - JVM metrics (related to GC and thread utilization)
    - JVM thread utilization – blocked, runnable, waiting connection use time

    **Application metrics**

    - HTTP/REST Controller metrics - calls
    - Service Metrics – Invocations
    - HTTP Client Metrics
    - Kafka broker metrics
    - Kafka messaging statics
    - JDBC connection pool metrics

    **Monitoring Tools**

    This set of tools can be use in combination for the integration, collection, persistetion and visualization of metrics, tipically used in combination to build views and dashboards for the end user.

    - Micrometer and JMX for the instrumention of the application to emit the metrics that are important for an effective monitoring.
    - Prometheus and/or DataDog for the colletion of metrics that the application emits and persisted them to provide advanced querying capability
    - Grafana for the visualization of the metrics collected by Prometheus and build reusability and intuitive views and dashboards. 
    - AWS Cloudwatch for the resource utilization metrics if it is cloud based architecture. Also cloudwatch has the capability to report alerts and notifications when metrics breach the defined thresholds.