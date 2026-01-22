import socket
from .constants import INTERNET_HOST, INTERNET_PORT, INTERNET_TIMEOUT, MSG_CONNECTION_ERROR


def isInternetConnected():
    try:
        host = socket.gethostbyname(INTERNET_HOST)
        s = socket.create_connection((host, INTERNET_PORT), INTERNET_TIMEOUT)
        shutDownConnection(s)
        return True
    except Exception as ex :
        print(MSG_CONNECTION_ERROR.format(error=ex))
        return False


def shutDownConnection(socket):
    socket.close()
