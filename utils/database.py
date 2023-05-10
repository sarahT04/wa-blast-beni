import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from .utils import format_number, ServerError

# Getting the data from .env file
from dotenv import load_dotenv
load_dotenv()

# DB Url
DB_URL = os.getenv('DB_URL')

# Create a new mongo client and connect to the server
client = MongoClient(DB_URL, server_api=ServerApi('1'))
# Defining the collection
phone_collection = client["wa-blast"]["datas"]

def get_data_with_range(start: int, stop: int) -> list:
    """Mendapatkan data sesuai dengan jangkauan yang diinginkan

    Args:
        start (int): Berapa angka pertama (contoh 2)
        stop (int): Sampai data terakhir (contoh 10)

    Returns:
        list: Data dari 2-10 (contoh)
    """
    return list(phone_collection.find({}).skip(start).limit(stop))
    

def get_all_data() -> list:
    """Memberikan semua data di database

    Returns:
        list: List dari semua data
    """
    return list(phone_collection.find({}))

def get_all_documents_count() -> int:
    """Memberikan banyaknya data di database

    Returns:
        int: Banyanknya data di database
    """
    return (phone_collection.count_documents({}))

def insert_data_formatted(name: str, phone: str) -> bool | str:
    """Insert data ke database

    Args:
        name (str): nama orang tersebut
        phone (str): nomor telf orang tersebut

    Raises:
        ServerError: bila data tidak bisa dimasukkan ke server
    """
    
    # Formatting the data
    data = {"name": name.title(), "phone": format_number(phone)}
    try:
        # Inserting it
        _ = phone_collection.insert_one(data)
        # If inserting has inserted_id, then it succesfully inserted.
        if _.inserted_id:
            print("Data ditambahkan di database!")
            return True
        raise ServerError
    except Exception as e:
        print(str(e))
        return str(e)
