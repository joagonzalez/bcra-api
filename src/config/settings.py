import os
from os.path import join, dirname
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

config = {
    "API_KEY": os.getenv('API_KEY'),
    "API_URL": os.getenv('API_URL'),
    "API_ENDPOINTS": {
        "USD_OF": os.getenv('ENDPOINTS_USD_OF'),
        "USD_BLUE": os.getenv('ENDPOINTS_USD_BLUE')
    }
}