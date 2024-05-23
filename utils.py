import socket


def isInternetConnected():
    try:
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        shutDownConnection(s)
        return True
    except:
        shutDownConnection(s)
        return False
    
def shutDownConnection(socket):
    socket.close()