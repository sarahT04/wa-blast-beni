from .utils import format_data, ServerError
from db.utils import client

def get_all_collection_names() -> list:
    """Mendapatkan semua nama koleksi di database

    Returns:
        list: Nama koleksi
    """
    return db.list_collection_names()

def get_data_with_range(start: int, stop: int) -> list:
    """Mendapatkan data sesuai dengan jangkauan yang diinginkan

    Args:
        start (int): Berapa angka pertama (contoh 2)
        stop (int): Sampai data terakhir (contoh 10)

    Returns:
        list: Data dari 2-10 (contoh)
    """
    return list(collection.find({}).skip(start).limit(stop))
    

def get_all_data() -> list:
    """Memberikan semua data di database

    Returns:
        list: List dari semua data
    """
    return list(collection.find({}))

def get_all_documents_count() -> int:
    """Memberikan banyaknya data di database

    Returns:
        int: Banyanknya data di database
    """
    return (collection.count_documents({}))

def insert_data_formatted(id: int, full_name: str, name: str, phone: str) -> bool | str:
    """Insert data ke database

    Args:
        name (str): nama orang tersebut
        phone (str): nomor telf orang tersebut

    Raises:
        ServerError: bila data tidak bisa dimasukkan ke server
    """
    # Formatting the data
    data = format_data(id, full_name, name, phone)
    try:
        # Inserting it
        _ = collection.insert_one(data)
        # If inserting has inserted_id, then it succesfully inserted.
        if _.inserted_id:
            print("Data ditambahkan di database!")
            return True
        raise ServerError
    except Exception as e:
        print(str(e))
        return str(e)


# Defining the collection
db = client["wa-blast"]
CURRENT_COLLECTION = get_all_collection_names()[0]
collection = db[CURRENT_COLLECTION]

# if __name__ == "__main__":
#     print(get_all_collection_names())