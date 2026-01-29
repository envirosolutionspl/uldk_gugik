import socket
from qgis.utils import iface
from qgis.core import Qgis

default_srid = 2180


def isInternetConnected():
    try:
        host = socket.gethostbyname("www.google.com")
        s = socket.create_connection((host, 80), 2)
        shutDownConnection(s)
        return True
    except Exception as e:
        iface.messageBar().pushMessage(
            "Ostrzeżenie:",
            f"Brak połączenia z internetem: {e}",
            level=Qgis.Warning,
            duration=10,
        )
        return False


def shutDownConnection(socket):
    socket.close()
