import socket
from .constants import CHECK_INTERNET_CLIENT


def isInternetConnected():
    try:
        host = socket.gethostbyname(CHECK_INTERNET_CLIENT["host"])
        s = socket.create_connection((host, CHECK_INTERNET_CLIENT["port"]), CHECK_INTERNET_CLIENT["timeout"])
        shutDownConnection(s)
        return True
    except Exception as ex:
        print(f"Błąd połączenia: {ex}")
        return False


def shutDownConnection(socket):
    socket.close()
