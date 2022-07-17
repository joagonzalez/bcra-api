from src.services.bcra import BCRA
from src.config.settings import config
from src.services.scheduler import Scheduler
from src.services.loggerService import logger
from prometheus_client import start_http_server


class Application():

    def __init__(self):
        logger.debug(f'config: {config}')
        self.scheduler = Scheduler()
        self.bcra_api = BCRA()

    def __del__(self):
        logger.debug('object destroyed')


    def run(self):
        '''
        Trigger main application
        '''
        logger.info('Starting application...')
        start_http_server(config['MONITORING']['PORT'])
        self.scheduler._schedule(param=config['BCRA_USD_OF'], job_name=self.bcra_api.get, time=1)
        self.scheduler.event_loop()
        