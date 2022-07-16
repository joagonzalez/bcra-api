import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

config = {
    "BCRA_API_KEY": os.getenv('BCRA_API_KEY'),
    "BCRA_API_URL": os.getenv('BCRA_API_URL'),
    "BCRA_USD_OF": os.getenv('BCRA_USD_OF'),
    "BCRA_USD_BLUE": os.getenv('BCRA_USD_BLUE'),
    "MONITORING": {
        "PORT": 8000
    }
}