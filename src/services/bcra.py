import requests
from src.config.settings import config
from src.services.loggerService import logger

class BCRA:
    def __init__(self) -> None:
        self.api = config['BCRA_API_URL']
        self.api_key = config['BCRA_API_KEY']
        self.usd_of = config['BCRA_USD_OF']
        self.usd_blue = config['BCRA_USD_BLUE']
        
    def __headers(self):
        return { 
                "Accept": "application/json",
                "Authorization": f"Bearer {self.api_key}"
                }
        
    def get(self, endpoint):
        if endpoint != None:
            api = self.api + '/' + endpoint
            logger.debug(f'request to {api}')
            result = requests.get(api, headers=self.__headers())
            logger.debug(f'result: {result.json()}')
            return result
        else:
            logger.error('No valid endpoint')
            return None