from urllib.parse import urlencode
from PyQt5.QtNetwork import QNetworkRequest, QNetworkAccessManager, QNetworkReply
from qgis.PyQt.QtCore import QUrl, QEventLoop

from qgis.core import QgsVectorLayer, QgsGeometry, QgsFeature, QgsProject

URL = "http://uldk.gugik.gov.pl/"


def getRequestTeryt(xy, request):
    def handleReply(reply):
        """"""
        nonlocal result
        nonlocal loop
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll().data().decode('utf-8')
            if data[0] !='0':
                return
            if ";" in data:
                result = data.split('\n')[1].split(';')[1]
            else:
                result = data.split('\n')[1]
        loop.quit()
    PARAMS = {'request': request, 'xy': xy, 'result': 'teryt'}    
    url = URL + "?" + urlencode(PARAMS)
    result = None
    request = QNetworkRequest(QUrl(url))
    manager = QNetworkAccessManager()
    reply = manager.get(request)
    reply.finished.connect(lambda: handleReply(reply))
    loop = QEventLoop()
    loop.exec_()
    return result