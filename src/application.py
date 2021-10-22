from src.config.settings import config

class Application():

    def __init__(self):
        print(f'config: {config}')


    def __del__(self):
        print('object destroyed')


    def run(self):
        '''
        Trigger main application
        '''
        print('Hello World!')