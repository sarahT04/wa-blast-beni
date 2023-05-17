def handle_exceptions(f):
    def wrapper(*args, **kw):
        try:
            return f(*args, **kw)
        except Exception as e:
            print(str(e))
        finally:
            print("Program selesai.")
    return wrapper

def format_time(time: str) -> tuple:
    return map(int, time.split(":"))

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

class ServerError(Exception):
    "Server error, coba lagi nanti"
    pass