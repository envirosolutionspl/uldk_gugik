import socket
from qgis.utils import iface
from qgis.core import Qgis
from qgis.PyQt.QtCore import QT_VERSION_STR
from .constants import CHECK_INTERNET_CLIENT

class VersionUtils:

    @staticmethod
    def isQt6():
        if QT_VERSION_STR.startswith('6'):
            return True
        else:
            return False

def isInternetConnected():
    try:
        host = socket.gethostbyname(CHECK_INTERNET_CLIENT["host"])
        s = socket.create_connection(
            (host, CHECK_INTERNET_CLIENT["port"]),
            CHECK_INTERNET_CLIENT["timeout"]
        )
        shutDownConnection(s)
        return True
    except Exception as ex:
        iface.messageBar().pushMessage(
            "Ostrzeżenie:",
            f"Brak połączenia z internetem: {ex}",
            level=Qgis.Warning,
            duration=10,
        )
        return False


def shutDownConnection(sock):
    sock.close()