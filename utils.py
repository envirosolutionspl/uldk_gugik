import socket

default_srid = 2180


def isInternetConnected():
    try:
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        shutDownConnection(s)
        return True
    except Exception:
        return False


def shutDownConnection(socket):
    socket.close()
