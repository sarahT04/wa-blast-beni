from datetime import datetime
from pywhatkit import *
from .utils import handle_exceptions, format_time

CLOSE_TIME = 1
WAIT_TIME = 5
CLOSE_TAB = True

@handle_exceptions
def send_message_with_image(number, msg, img_path):
    print("Bekerja...")
    sendwhats_image(receiver=number, img_path=img_path, caption=msg, close_time=CLOSE_TIME, wait_time=WAIT_TIME, tab_close=CLOSE_TAB)

@handle_exceptions
def send_instant_message(phone: str, msg: str) -> None:
    """Mengirim pesan secara langsung

    Args:
        phone (str): Nomor telfon
        msg (str): Pesan yang ingin dikirim.
    """
    print("Bekerja...")
    sendwhatmsg_instantly(phone_no=phone, message=msg, close_time=CLOSE_TIME, tab_close=CLOSE_TAB)

@handle_exceptions
def send_scheduled_message(phone: str, msg: str, time: str) -> None:
    """Mengirim pesan yang dijadwalkan

    Args:
        phone (str): Nomor telfon
        msg (str): Pesan yang ingin dikirim.
        time (str): Waktu yang dijadwalkan.
    """
    
    hours, minutes = format_time(time=time)
    print("Bekerja...")
    sendwhatmsg(phone_no=phone, message=msg, time_hour=hours, time_min=minutes, close_time=CLOSE_TIME, wait_time=WAIT_TIME, tab_close=CLOSE_TAB)


@handle_exceptions
def send_to_group(group_id: str, msg: str, instant:bool=True, time: str= datetime.now().strftime('%H:%M')) -> None:
    """Kirim pesan ke group.

    Args:
        group_id (str): Taruh ID group disini. bisa check ID grup di invite link.  
        msg (str): pesan yang ingin dikirim  
        time (str): waktu mulai broadcast. format 24H seperti "13:30" (jam setengah 2).  
    """
    hours, minutes = format_time(time=time)
    print("Bekerja...")
    sendwhatmsg_to_group(group_id=group_id, message=msg, time_hour=hours, time_min=minutes, close_time=CLOSE_TIME, wait_time=WAIT_TIME, tab_close=CLOSE_TAB)
