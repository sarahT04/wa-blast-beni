from utils.database import *
from utils.functions import *

def add_data(name: str, phone: str) -> bool | str:
    """Tambahkan data ke database

    Args:
        name (str): Nama orang
        phone (str): Nomor telf orang

    Returns:
        bool: bila berhasil
        str: pesan error bila tidak berhasil
    """
    return insert_data_formatted(name, phone)

def send_message_handler(datas: list, msg: str) -> bool | str:
    for data in datas:
        phone = format_number(data["phone"])
        try:
            send_instant_message(phone, msg)
        except Exception as e:
            return str(e)
    return True

def send_with_picture(msg: str, img_path: str, ranged=False, start: int=0, stop: int=10) -> bool | str:
    """Kirim pesan dengan gambar

    Args:
        msg (str): Pesan yang ingin dikirim
        img_path (str): Path ke file image (ex: C://Users/BENI/image.png)
        ranged (bool, optional): Bila menggunakan range. Defaults to False.
        start (int, optional): Mulai dari. Defaults to 0.
        stop (int, optional): Sampai dengan. Defaults to 10.

    Returns:
        bool: bila berhasil
        str: pesan error bila tidak berhasil
    """
    if ranged is True:
        datas = get_data_with_range(start, stop)
    else:
        datas = get_all_data()
    for data in datas:
        phone = format_number(data["phone"])
        try:
            send_message_with_image(phone, msg, img_path)
        except Exception as e:
            return str(e)
    return True

def send_in_range(msg: str, start: int, stop: int) -> bool | str:
    """Kirim pesan dengan range

    Args:
        msg (str): Pesan yang ingin dikirim
        start (int): Mulai dari
        stop (int): Sampai dengan

    Returns:
        bool: bila berhasil
        str: pesan error bila tidak berhasil
    """
    datas = get_data_with_range(start, stop)
    return send_message_handler(datas, msg)

def send_to_all(msg: str) -> bool | str:
    """Kirim pesan kepada semua yang ada di database

    Args:
        msg (str): Pesan

    Returns:
        bool: bila berhasil
        str: pesan error bila tidak berhasil
    """
    datas = get_all_data()
    return send_message_handler(datas, msg)
