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

class MessageUtils:
    
    @staticmethod
    def pushSuccess(iface, message: str) -> None:
        iface.messageBar().pushMessage(
            "Sukces:",
            message,
            level=Qgis.Success,
            duration=10
        )

    @staticmethod
    def pushInfo(iface, message: str) -> None:
        iface.messageBar().pushMessage(
            'Informacja',
            message,
            level=Qgis.Info,
            duration=10
        )

    @staticmethod
    def pushWarning(iface, message: str) -> None:
        iface.messageBar().pushMessage(
            "Ostrzeżenie",
            message,
            level=Qgis.Warning,
            duration=10
        )
    
    @staticmethod
    def pushCritical(iface, message: str) -> None:
        iface.messageBar().pushMessage(
            message,
            level=Qgis.Critical,
            duration=10
        )

    @staticmethod
    def pushLogSuccess(message: str) -> None:
        QgsMessageLog.logMessage(
            message,
            tag=PLUGIN_NAME,
            level=Qgis.Success
        )

    @staticmethod
    def pushLogInfo(message: str) -> None:
        QgsMessageLog.logMessage(
            message,
            tag=PLUGIN_NAME,
            level=Qgis.Info
        )
    
    @staticmethod
    def pushLogWarning(message: str) -> None:
        QgsMessageLog.logMessage(
            message,
            tag=PLUGIN_NAME,
            level=Qgis.Warning
        )
    
    @staticmethod
    def pushLogCritical(message: str) -> None:
        QgsMessageLog.logMessage(
            message,
            tag=PLUGIN_NAME,
            level=Qgis.Critical
        )

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
