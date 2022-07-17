from prometheus_client import Summary, Gauge, Histogram, Counter

class Monitoring:
    def __init__(self):
        # Create a metric to track time spent and requests made.
        self.usd_of = Gauge('bcra_usd_of', 'Current value of official dolar value')
        self.usd_blue = Gauge('bcra_usd_blue', 'Current value of non official dolar value')
        self.request_time = Summary('request_processing_seconds', 'Time spent processing request')
        
monitor = Monitoring()
