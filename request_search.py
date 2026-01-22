from urllib.parse import urlencode
from PyQt5.QtNetwork import QNetworkRequest, QNetworkAccessManager, QNetworkReply
from qgis.PyQt.QtCore import QUrl, QEventLoop
from .uldk_gugik_dialog import UldkGugikDialog
from .constants import ULDK_BASE_URL, ULDK_NO_RESULTS, ULDK_MIN_LINE_LEN

class Request:

    def __init__(self, params):
        self.params = params
        self._data = set()
        self.url = ULDK_BASE_URL
        self.manager = QNetworkAccessManager()

        self.getRequest()
        self.loop = QEventLoop()
        self.loop.exec_()


    def getRequest(self):
        """Wysłanie zapytania z odpowiednimi parametrami"""
        final_url = self.url + "?" + urlencode(self.params)
        req = QNetworkRequest(QUrl(final_url))
        reply = self.manager.get(req)
        reply.finished.connect(lambda: self.handleRequest(reply))
        

    def handleRequest(self, reply):
        """Obsłużenie odpowiedzi"""
        self._data.clear()
        if reply.error() == QNetworkReply.NoError:
            returned_data = reply.readAll().data().decode('utf-8')
            for line in returned_data.split('\n'):
                if len(line) < ULDK_MIN_LINE_LEN :
                    pass
                if line == ULDK_NO_RESULTS:
                    pass
                else:
                    self._data.add(line.replace('\r',''))
        self.loop.quit()

    @property
    def data(self):
        return self._data