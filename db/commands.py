import csv
from utils import client, format_data

FILE_PATH = './datas.csv'
db = client['wa-blast']

def insert_bulk_datas(file_path: str):
    datas = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        # data is
        # sarah,sarah xxxx,62xxxxxxxx,nama_db
        for data in reader:
            # Format all the data in the reader
            nama_panjang, nama, nomor, nama_db = data
            if nama_db not in datas:
                datas[nama_db] = []
            x = len(datas[nama_db]) + 1
            datas[nama_db].append(format_data(x, nama_panjang, nama, nomor))
    # Insert all to database
    try:
        print("Tunggu.. data sedang dimasukkan ke database...")
        for db_name in datas.keys():
            data = datas[db_name]
            col = db[db_name]
            col.insert_many(data)
        print("Data telah dimasukkan ke database.")
    except Exception as e:
        print(f"Error: {str(e)}")

def setup() -> None:
    """Setup untuk menghapus semua koleksi dan menambahkan yang diinginkan."""
    try:
        # Get a list of existing collections
        collections = db.list_collection_names()
        # and delete the collections
        for collection in collections:
            db[collection].drop()
        insert_bulk_datas(FILE_PATH)
    except Exception as e:
        print(str(e))

def ping_db():
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    try:
        while True:
            user_input = input('Mau setup atau tambah data? [setup/tambah]: ')
            if user_input == "setup":
                setup()
                dbs = db.list_collection_names()
                for name in dbs:
                    print(list(db[name].find({})))
            elif user_input == "tambah":
                insert_bulk_datas(FILE_PATH)
                print('Selesai')
            else:
                print("Tolong tulis hanya 'setup' atau 'tambah'.")
    except Exception as e:
        print("Error: ")
        print(str(e))
    