from urllib.parse import urlencode
from PyQt5.QtNetwork import QNetworkRequest, QNetworkAccessManager, QNetworkReply
from qgis.PyQt.QtCore import QUrl, QEventLoop


class Request:
    def __init__(self, params,objectType, **kwargs):
        self.params = params
        self._data = None
        self.url = "http://uldk.gugik.gov.pl/"
        self.manager = QNetworkAccessManager()

        self.teryt = kwargs.get('teryt', None)
        self.objectType = objectType

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
            print(returnedData)
            for line in returnedData.split('\n'):
                if len(line) < 3 or line == "-1 brak wyników" or line.find("XML")>-1 or line.find("błęd")>-1:
                    continue
                if ";" in line:
                    polygon = line.split(';')[1]
                    if not self.teryt:
                        self._data = polygon
                        pass
                    
                    if self.objectType == 1:
                        teryt = polygon.split('|')[1].split('.')[0]
                        break
                    elif self.objectType ==2:
                        if polygon.split('|')[1].find(".") >-1:
                            teryt = polygon.split('|')[1].split('.')[0]
                            break
                        else:
                            pass
                    else:
                        teryt = polygon.split('|')[1]
                        break

                    if teryt[:-4] == self.teryt[:-4]:
                        # jeżeli wybór przezXY lub teryt z formularza == teryt otrzymany z odpowiedzi
                        self._data = polygon
                        break

                else:
                    if not self.teryt:
                        self._data = line
                        pass

                    if self.objectType == 1:
                        try:
                            teryt = line.split('|')[1].split('.')[0]
                        except IndexError:
                            pass
                        break

                    elif self.objectType ==2:
                        if line.split('|')[1].find(".") >-1:
                            teryt = line.split('|')[1].split('.')[0]
                            break
                        else:
                            pass
                    else:
                        teryt = line.split('|')[1].split('.')[0]
                    if teryt[:-4] == self.teryt[:-4]:
                        self._data = line
                        break

        else:  # brak zgodności - nie ma takiego nr działki
            self._data = None

        self.loop.quit()

    @property
    def data(self):
        return self._data