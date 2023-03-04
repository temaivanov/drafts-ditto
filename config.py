#Flask configuration 

from os import environ, path
from dotenv import load_dotenv

SECRET_KEY = environ.get('SECRET_KEY')

