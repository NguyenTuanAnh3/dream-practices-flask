import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseConfig():
    DATABASE_HOST = os.getenv('DATABASE_HOST')
    DATABASE_POST = os.getenv('DATABASE_POST')
    DATABASE_NAME = os.getenv('DATABASE_NAME')
    DATABASE_USER = os.getenv('DATABASE_USER')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')