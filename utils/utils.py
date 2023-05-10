def handle_exceptions(f):
    def wrapper(*args, **kw):
        try:
            return f(*args, **kw)
        except CountryCodeException:
            print("Nomor yang anda berikan kurang tepat.")
        except InternetException:
            print("Internet lambat. Coba kembali nanti.")
        except CallTimeException:
            print("Program menunggu terlalu lama.")
        finally:
            print("Program selesai.")
    return wrapper

def format_time(time: str) -> tuple:
    return map(int, time.split(":"))

def format_number(number: str) -> str:
    formatted_number = ''.join(number.replace('-', ' ').split(' '))
    if number.startswith("+"):
        return formatted_number
    return "+" + formatted_number

class ServerError(Exception):
    "Server error, coba lagi nanti"
    pass