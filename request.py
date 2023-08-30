from urllib.parse import urlencode
from PyQt5.QtNetwork import QNetworkRequest, QNetworkAccessManager, QNetworkReply
from PyQt5.QtCore import QUrl, QEventLoop



class Request:
    
    def __init__(self, params):
        self.params = params
        self._data = None
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
        if reply.error() == QNetworkReply.NoError:
            returnedData = reply.readAll().data().decode('utf-8')
            if returnedData[0] == '0':
                return
            if ';' in returnedData:
                self._data = returnedData.split('\n')[1].split(';')[1]
            else:
                self._data = returnedData.split('\n')[1]
        self.loop.quit()
    
    @property
    def data(self):
        return self._data
