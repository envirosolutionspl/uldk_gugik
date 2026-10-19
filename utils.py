import os
import socket
from qgis.utils import iface
from qgis.core import Qgis, QgsMessageLog, QgsApplication
from qgis.PyQt.QtCore import QT_VERSION_STR, Qt
from qgis.PyQt.QtGui import QPalette, QPixmap
from qgis.PyQt.QtWidgets import QWidget
from .constants import CHECK_INTERNET_CLIENT
from . import PLUGIN_NAME

PLUGIN_DIR = os.path.dirname(__file__)

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

class ThemeUtils:
    """Wspólne dla okien wtyczki (główne okno, okno QGIS Feed): motyw jasny/ciemny i logo."""

    @staticmethod
    def isDarkTheme():
        """Ciemny motyw QGIS (np. Night Mapping) albo ciemna paleta systemu."""
        name = ''  # domyślnie - gdy QGIS nie poda nazwy motywu albo wystąpi wyjątek
        try:
            theme_name = (QgsApplication.themeName() or '').lower()
            if theme_name:
                name = theme_name.lower()
        except AttributeError as e:
            MessageUtils.pushLogCritical(f"Atrybut motywu jest niedostępny (AttributeError): {e}")
        except RuntimeError as e:
            MessageUtils.pushLogCritical(f"Aplikacja QGIS nie jest w pełni zainicjalizowana (RuntimeError): {e}")
        except TypeError as e:
            MessageUtils.pushLogCritical(f"Nieoczekiwany typ danych przy pobieraniu motywu (TypeError): {e}")
        except Exception as e:
            MessageUtils.pushLogCritical(f"Nieoczekiwany błąd: {e}")

        if 'night' in name or 'dark' in name:
            return True
        return QgsApplication.palette().color(QPalette.ColorRole.Window).lightness() < 128

    @staticmethod
    def repolishAll(window):
        """Pełne przeliczenie stylu okna i wszystkich jego widgetów (po zmianie właściwości "theme").
        Widgety mogły zostać ostylowane, zanim okno dostało tę właściwość (setStyleSheet sam tego nie robi przed show())."""
        for widget in [window] + window.findChildren(QWidget):
            widget.style().unpolish(widget)
            widget.style().polish(widget)
            widget.update()

    @staticmethod
    def setLogo(label, filename, height):
        """Wstawia logo z images/ do etykiety, w skali ekranu (bez rozpikselowania przy 125-150%)."""
        pix = QPixmap(os.path.join(PLUGIN_DIR, 'images', filename))
        if pix.isNull():
            return
        dpr = label.devicePixelRatioF()
        pix = pix.scaledToHeight(int(height * dpr), Qt.TransformationMode.SmoothTransformation)
        pix.setDevicePixelRatio(dpr)
        label.setScaledContents(False)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setPixmap(pix)

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
