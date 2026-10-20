from urllib.parse import urlencode
from qgis.PyQt.QtNetwork import QNetworkReply
from qgis.PyQt.QtCore import QEventLoop

from .https_adapter import LegacySession
from .uldk_gugik_dialog import UldkGugikDialog
from .constants import ULDK_BASE_URL, ULDK_NO_RESULTS, ULDK_MIN_LINE_LEN

# Qt5/Qt6 compat: QEventLoop.exec_ -> exec
if not hasattr(QEventLoop, 'exec'):
    QEventLoop.exec = QEventLoop.exec_


class Request:
    def __init__(self, params):
        self.params = params
        self._data = set()

        self.url = ULDK_BASE_URL
        self.session = LegacySession()

        self.loop = QEventLoop()
        self.reply = None

        self.getRequest()
        self.loop.exec()

    def getRequest(self):
        final_url = f"{self.url}?{urlencode(self.params)}"
        self.reply = self.session.get(final_url)
        self.reply.finished.connect(lambda: self.handleRequest(self.reply))

    def handleRequest(self, reply):
        """Obsłużenie odpowiedzi (Qt5/Qt6 kompatybilnie + constants)"""
        try:
            self._data.clear()

            # Qt5/Qt6 safe: sprawdzanie błędu
            error_val = reply.error()
            if hasattr(QNetworkReply, 'NetworkError'):
                no_err = QNetworkReply.NetworkError.NoError  # Qt6
                is_no_error = (error_val == no_err)
            else:
                no_err = QNetworkReply.NoError  # Qt5
                is_no_error = (int(error_val) == int(no_err))

            if not is_no_error:
                return

            # Odczyt danych (Qt5/Qt6)
            read_data = reply.readAll()
            if hasattr(read_data, 'data'):
                returned_data = read_data.data().decode('utf-8')
            else:
                returned_data = bytes(read_data).decode('utf-8')

            for line in returned_data.split('\n'):
                line = line.replace('\r', '')

                if len(line) < ULDK_MIN_LINE_LEN:
                    continue
                if line == ULDK_NO_RESULTS:
                    continue

                self._data.add(line)

        except Exception:
            pass
        finally:
            if self.loop.isRunning():
                self.loop.quit()
            reply.deleteLater()

    @property
    def data(self):
        return self._data