from prometheus_client import Summary, Gauge, Histogram, Counter

class Monitoring:
    def __init__(self):
        # Create a metric to track time spent and requests made.
        self.request_time = Summary('request_processing_seconds', 'Time spent processing request')
        
        
monitor = Monitoring()
