
with Diagram("Advanced Web Service with On-Premise", show=False):
    ingress = Nginx("ingress")
    
    metrics = Prometheus("metric")
    metrics << Grafana("monitoring")
    
    with Cluster("Service Cluster"):
         grpcsvc = [
            Server("grpc1"),
            Server("grpc2"),
            Server("grpc3")]

    with Cluster("Sessions HA"):
        primary = Redis("session")
        primary - Redis("replica") << metrics
        grpcsvc >> primary
    
    aggregator = Fluentd("Logging")
    aggregator >> Kafka("stream") >> Spark("Analytics")
    
    ingress >> grpcsvc >> aggregator
