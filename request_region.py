from urllib.parse import urlencode
from qgis.PyQt.QtNetwork import QNetworkReply
from qgis.PyQt.QtCore import QEventLoop
from .https_adapter import getLegacySession
from .uldk_gugik_dialog import UldkGugikDialog

if not hasattr(QEventLoop, 'exec'):
    QEventLoop.exec = QEventLoop.exec_


class Request:
    def __init__(self, params):
        self.params = params
        self._data = set()
        self.url = "https://uldk.gugik.gov.pl/"
        self.session = getLegacySession()
        
        
        self.loop = QEventLoop()
        self.reply = None

        self.getRequest()
        self.loop.exec()
    def getRequest(self):
        final_url = self.url + "?" + urlencode(self.params)
        self.reply = self.session.get(final_url)
        self.reply.finished.connect(lambda: self.handleRequest(self.reply))
        

    def handleRequest(self, reply):
        """Obsłużenie odpowiedzi"""
        try:
            self._data.clear()
            error_val = reply.error()
            if hasattr(QNetworkReply, 'NetworkError'):
                no_err = QNetworkReply.NetworkError.NoError  # Qt6
                is_no_error = (error_val == no_err)  # W Qt6 porównujemy enumy bezpośrednio
            else:
                no_err = QNetworkReply.NoError  # Qt5
                is_no_error = (int(error_val) == int(no_err))  # W Qt5 konwertujemy na int
            if is_no_error:
                returned_data = reply.readAll().data().decode('utf-8')
                for line in returned_data.split('\n'):
                    if len(line) < 3:
                        continue
                    if line == "-1 brak wyników":
                        continue
                    self._data.add(line.replace('\r',''))
        except Exception:
            pass
        finally:
            # Zawsze zakończ loop, nawet w przypadku błędu
            if self.loop.isRunning():
                self.loop.quit()
            reply.deleteLater()

    @property
    def data(self):
        return self._data