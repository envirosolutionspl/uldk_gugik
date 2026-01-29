from urllib.parse import urlencode
from PyQt5.QtNetwork import QNetworkRequest, QNetworkAccessManager, QNetworkReply
from qgis.PyQt.QtCore import QUrl, QEventLoop
from .constants import (
    ULDK_BASE_URL, ULDK_NO_RESULTS, ULDK_XML_MARKER, ULDK_ERROR_MARKERS, 
    ENCODING_SYSTEM, ULDK_MIN_LINE_LEN, ULDK_OBJ_REGION, ULDK_NOT_FOUND,
    ULDK_TERYT_SUFFIX_LEN
)

class Request:
    def __init__(self, params,object_type, **kwargs):
        self.params = params
        self._data = None
        self.url = ULDK_BASE_URL
        self.manager = QNetworkAccessManager()

        self.teryt = kwargs.get('teryt', None)
        self.object_type = object_type

        self.getRequest()
        self.loop = QEventLoop()
        self.loop.exec_()

    def getRequest(self):
        """Wysłanie zapytania z odpowiednimi parametrami"""
        final_url = f"{self.url}?{urlencode(self.params)}"
        req = QNetworkRequest(QUrl(final_url))
        reply = self.manager.get(req)
        reply.finished.connect(lambda: self.handleRequest(reply))

    def handleRequest(self, reply):
        """Obsłużenie odpowiedzi"""
        if reply.error() == QNetworkReply.NoError:
            returnedData = reply.readAll().data().decode(ENCODING_SYSTEM)

            for line in returned_data.split('\n'):
                if len(line) < ULDK_MIN_LINE_LEN or line == ULDK_NO_RESULTS or line.find(ULDK_XML_MARKER)> ULDK_NOT_FOUND or any(line.find(marker) > ULDK_NOT_FOUND for marker in ULDK_ERROR_MARKERS):
                    continue
                if ";" in line:
                    polygon = line.split(';')[1]
                    if not self.teryt:
                        self._data = polygon
                        pass
                    
                    if self.object_type in [1, 6]:
                        teryt = polygon.split('|')[1].split('.')[0]
                        break
                    elif self.object_type == ULDK_OBJ_REGION:
                        if polygon.split("|")[1].find(".") > ULDK_NOT_FOUND:
                            teryt = polygon.split("|")[1].split(".")[0]
                            break
                        else:
                            pass
                    else:
                        teryt = polygon.split('|')[1]
                        break

                    if teryt[:-ULDK_TERYT_SUFFIX_LEN] == self.teryt[:-ULDK_TERYT_SUFFIX_LEN]:
                        # jeżeli wybór przezXY lub teryt z formularza == teryt otrzymany z odpowiedzi
                        self._data = polygon
                        break

                else:
                    if not self.teryt:
                        self._data = line
                        pass

                    if self.object_type in [1, 6]:
                        try:
                            teryt = line.split('|')[1].split('.')[0]
                        except IndexError:
                            pass
                        break

                    elif self.object_type == ULDK_OBJ_REGION:
                        if line.split("|")[1].find(".") >ULDK_NOT_FOUND:
                            teryt = line.split("|")[1].split(".")[0]
                            break
                        else:
                            pass
                    else:
                        teryt = line.split("|")[1].split(".")[0]
                    if teryt[:-ULDK_TERYT_SUFFIX_LEN] == self.teryt[:-ULDK_TERYT_SUFFIX_LEN]:
                        self._data = line
                        break

        else:  # brak zgodności - nie ma takiego nr działki
            self._data = None

        self.loop.quit()

    @property
    def data(self):
        return self._data