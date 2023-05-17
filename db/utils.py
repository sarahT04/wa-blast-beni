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

def format_number(number: str) -> str:
    # in case any non ascii character ignore it and replace any dash with whitespace and remove any whitespaces and dash
    formatted_number = number.encode('ascii', 'ignore').decode('utf-8').replace('-', '').replace(' ', '')
    if formatted_number.startswith("+"):
        return formatted_number
    return "+" + formatted_number

def format_name(name: str) -> str:
    return name.encode('ascii', 'ignore').decode('utf-8').title()

def format_data(id: int, full_name: str, name: str, phone: str):
    return { "_id": id, "nama_panjang" : format_name(full_name), "nama" : format_name(name), "nomor" : format_number(phone) }