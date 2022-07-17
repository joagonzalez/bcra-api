import time
import schedule
from src.services.loggerService import logger


class Scheduler():
    def __init__(self):
        self.scheduler = schedule
    
    def job(self):
        print("I'm working...")
        
    def _schedule(self, param=None, job_name=None, time=5):
        logger.debug(f'Scheduling job: param={param} - job_name={job_name} - time={time}')
        self.scheduler.every(time).minutes.do(job_name, param)
        
    def job_status(self, job_name=None):
        pass

    def event_loop(self):
        while True:
            self.scheduler.run_pending()
            time.sleep(1)


if __name__ == "__main__":
    pass