from utils.database import *
from utils.functions import *
import os

def get_image_path(img_name: str) -> str:
    current_path = os.getcwd()
    image_path = os.path.join(current_path, "img", img_name)
    return image_path

def add_data(collection_name: str, full_name: str, name: str, phone: str) -> bool | str:
    """Tambahkan data ke database

    Args:
        name (str): Nama orang
        phone (str): Nomor telf orang

    Returns:
        bool: bila berhasil
        str: pesan error bila tidak berhasil
    """
    _id = get_all_documents_count(collection_name) + 1
    return insert_data_formatted(_id, full_name, name, phone)

def send_message_handler(datas: list, msg: str, img_path: str | bool=False) -> bool | str:
    for data in datas:
        _id, full_name, name, phone = data.values()
        new_msg = msg.format(nama=name, nama_panjang=full_name)
        try:
            if img_path is not False:
                send_message_with_image(phone, new_msg, r"{}".format(get_image_path(img_path)))
            else:
                send_instant_message(phone, new_msg)
        except Exception as e:
            return str(e)
    return True

def send_with_picture(collection_name: str, msg: str, img_path: str, ranged=False, start: int=0, stop: int=10) -> bool | str:
    """Kirim pesan dengan gambar

    Args:
        msg (str): Pesan yang ingin dikirim
        img_path (str): Path ke file image di folder /img/ di program ini.
        ranged (bool, optional): Bila menggunakan range. Defaults to False.
        start (int, optional): Mulai dari. Defaults to 0.
        stop (int, optional): Sampai dengan. Defaults to 10.

    Returns:
        bool: bila berhasil
        str: pesan error bila tidak berhasil
    """
    if ranged is True:
        datas = get_data_with_range(collection_name, start, stop)
    else:
        datas = get_all_data(collection_name)
    return send_message_handler(datas, msg, img_path)

def send_in_range(collection_name: str, msg: str, start: int, stop: int) -> bool | str:
    """Kirim pesan dengan range

    Args:
        msg (str): Pesan yang ingin dikirim
        start (int): Mulai dari
        stop (int): Sampai dengan

    Returns:
        bool: bila berhasil
        str: pesan error bila tidak berhasil
    """
    datas = get_data_with_range(collection_name, start, stop)
    return send_message_handler(datas, msg)

def send_to_all(collection_name: str, msg: str) -> bool | str:
    """Kirim pesan kepada semua yang ada di database

    Args:
        msg (str): Pesan

    Returns:
        bool: bila berhasil
        str: pesan error bila tidak berhasil
    """
    datas = get_all_data(collection_name)
    return send_message_handler(datas, msg)

if __name__ == '__main__':
    send_to_all("cfi", "hi {nama}!")