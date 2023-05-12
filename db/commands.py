import pymongo
from .utils import client
from ..utils.database import insert_data_formatted

db = client['wa-blast']

def insert_bulk_datas(id, full_name, name, phone, collection_name):
    pass
    # with open csv
    # for data in datas:
        # data = format_data(id, full_name, name, phone)
        # use which collection
        # insert one formatted


def setup():
    db['datas'].rename('sahabat')

def ping_db():
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)