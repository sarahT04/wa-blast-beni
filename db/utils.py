import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Getting the data from .env file
from dotenv import load_dotenv
load_dotenv()

# DB Url
DB_URL = os.getenv('DB_URL')

# Create a new mongo client and connect to the server
client = MongoClient(DB_URL, server_api=ServerApi('1'))
