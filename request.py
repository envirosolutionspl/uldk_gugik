from urllib.parse import urlencode
from qgis.PyQt.QtNetwork import QNetworkReply
from qgis.PyQt.QtCore import QEventLoop
from qgis.utils import iface

from .https_adapter import getLegacySession
from .constants import (
    ULDK_BASE_URL, ULDK_NO_RESULTS, ULDK_XML_MARKER, ULDK_ERROR_MARKERS,
    ENCODING_SYSTEM, ULDK_MIN_LINE_LEN, ULDK_OBJ_REGION, ULDK_NOT_FOUND,
    ULDK_TERYT_SUFFIX_LEN
)

# Qt5/Qt6 compat: QEventLoop.exec_ -> exec
if not hasattr(QEventLoop, 'exec'):
    QEventLoop.exec = QEventLoop.exec_


class Request:
    def __init__(self, params, object_type, **kwargs):
        self.params = params
        self._data = None
        self.session = getLegacySession()
        self.url = ULDK_BASE_URL

        self.teryt = kwargs.get('teryt', None)
        self.object_type = object_type

        # Utworzenie loop PRZED wywołaniem request
        self.loop = QEventLoop()
        self.reply = None

        self.getRequest()
        self.loop.exec()

    def getRequest(self):
        try:
            final_url = f"{self.url}?{urlencode(self.params)}"
        except Exception as e:
            iface.messageBar().pushWarning(
                "ULDK",
                f"Nie udało się zbudować adresu zapytania: {e}",
            )
            self._data = None
            return

        try:
            self.reply = self.session.get(final_url)
        except Exception as e:
            iface.messageBar().pushWarning(
                "ULDK",
                f"Błąd podczas wysyłania zapytania do ULDK: {e}",
            )
            self._data = None
            return

        if not self.reply:
            iface.messageBar().pushWarning(
                "ULDK",
                "Serwer ULDK nie zwrócił odpowiedzi.",
            )
            self._data = None
            return

        # Czekamy na zakończenie odpowiedzi
        self.reply.finished.connect(self.handleReply)

    def handleReply(self):
        """Obsłużenie odpowiedzi (Qt5/Qt6 kompatybilnie + logika constants)"""
        reply = self.reply
        try:
            # Sprawdzenie błędu w sposób zgodny z Qt5 i Qt6
            error_val = reply.error()
            if hasattr(QNetworkReply, 'NetworkError'):
                no_err = QNetworkReply.NetworkError.NoError  # Qt6
                is_no_error = (error_val == no_err)
            else:
                no_err = QNetworkReply.NoError  # Qt5
                is_no_error = (int(error_val) == int(no_err))

            if not is_no_error:
                iface.messageBar().pushWarning(
                    "ULDK",
                    f"Błąd sieci podczas pobierania danych z ULDK: {reply.errorString()}",
                )
                self._data = None
                return

            # Odczyt danych (działa i w Qt5, i w Qt6)
            read_data = reply.readAll()
            if hasattr(read_data, 'data'):
                returned_data = read_data.data().decode(ENCODING_SYSTEM)
            else:
                returned_data = bytes(read_data).decode(ENCODING_SYSTEM)

            if not returned_data or len(returned_data.strip()) == 0:
                iface.messageBar().pushWarning(
                    "ULDK",
                    "Serwer ULDK zwrócił pustą odpowiedź.",
                )
                self._data = None
                return

            teryt = None

            for line in returned_data.split('\n'):
                if (
                    len(line) < ULDK_MIN_LINE_LEN
                    or line == ULDK_NO_RESULTS
                    or line.find(ULDK_XML_MARKER) > ULDK_NOT_FOUND
                    or any(line.find(marker) > ULDK_NOT_FOUND for marker in ULDK_ERROR_MARKERS)
                ):
                    continue

                if ";" in line:
                    polygon = line.split(';')[1]
                else:
                    polygon = line
                    
                if not self.teryt:
                    self._data = polygon
                    break

                if self.object_type in [1, 6]:
                    try:
                        teryt = polygon.split('|')[1].split('.')[0]
                    except IndexError:
                        continue

                elif self.object_type == ULDK_OBJ_REGION:
                    try:
                        field = polygon.split("|")[1]
                    except IndexError:
                        continue

                    if field.find(".") > ULDK_NOT_FOUND:
                        teryt = field.split(".")[0]
                    else:
                        continue

                else:
                    try:
                        teryt = polygon.split('|')[1]
                    except IndexError:
                        continue
                        
                if (
                    teryt
                    and self.teryt
                    and teryt[:-ULDK_TERYT_SUFFIX_LEN] == self.teryt[:-ULDK_TERYT_SUFFIX_LEN]
                ):
                    self._data = polygon
                    break

            if self._data is None:
                iface.messageBar().pushWarning(
                    "ULDK",
                    "Brak wyników dla podanego zapytania do ULDK.",
                )

        except Exception as e:
            iface.messageBar().pushWarning(
                "ULDK",
                f"Nieoczekiwany błąd podczas przetwarzania odpowiedzi ULDK: {e}",
            )
            self._data = None
        finally:
            if self.loop.isRunning():
                self.loop.quit()
            reply.deleteLater()

    @property
    def data(self):
        return self._data
