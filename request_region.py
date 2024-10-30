from urllib.parse import urlencode
from PyQt5.QtNetwork import QNetworkRequest, QNetworkAccessManager, QNetworkReply
from qgis.PyQt.QtCore import QUrl, QEventLoop
from .uldk_gugik_dialog import UldkGugikDialog


class Request:
    def __init__(self, params):
        self.params = params
        self._data = set()
        self.url = "http://uldk.gugik.gov.pl/"
        self.manager = QNetworkAccessManager()

        self.getRequest()
        self.loop = QEventLoop()
        self.loop.exec_()
    def getRequest(self):
        """Wysłanie zapytania z odpowiednimi parametrami"""
        finalUrl = self.url + "?" + urlencode(self.params)
        req = QNetworkRequest(QUrl(finalUrl))
        reply = self.manager.get(req)
        reply.finished.connect(lambda: self.handleRequest(reply))
        

    def handleRequest(self, reply):
        """Obsłużenie odpowiedzi"""
        self._data.clear()
        if reply.error() == QNetworkReply.NoError:
            returnedData = reply.readAll().data().decode('utf-8')
            for line in returnedData.split('\n'):
                if len(line) < 3 :
                    pass
                if line in "-1 brak wyników":
                    pass
                else:
                    self._data.add(line.replace('\r',''))
        self.loop.quit()

    @property
    def data(self):
        return self._data