import warnings
import ssl

from qgis.core import QgsNetworkAccessManager
from qgis.PyQt.QtNetwork import QNetworkRequest, QNetworkReply, QSslConfiguration, QSslSocket
from qgis.PyQt.QtCore import QUrl, QEventLoop

# Qt5/Qt6 compat
if not hasattr(QEventLoop, 'exec'):
    QEventLoop.exec = QEventLoop.exec_


class CustomHttpAdapter:
    def __init__(self, ssl_context=None, **kwargs):
        self.ssl_context = ssl_context

    def configureRequest(self, request):
        ssl_conf = request.sslConfiguration()
        if ssl_conf.isNull():
            ssl_conf = QSslConfiguration.defaultConfiguration()
        if hasattr(QSslSocket, 'PeerVerifyMode'):
            verify_mode = QSslSocket.PeerVerifyMode.VerifyNone  # Qt6
        else:
            verify_mode = QSslSocket.VerifyNone  # Qt5
        ssl_conf.setPeerVerifyMode(verify_mode)
        ssl_conf.setPeerVerifyDepth(0)
        request.setSslConfiguration(ssl_conf)
        return request


class LegacySession:
    def __init__(self):
        warnings.filterwarnings("ignore", category=ResourceWarning)
        ctx = ssl.create_default_context()
        self.adapter = CustomHttpAdapter(ctx)
        self.manager = QgsNetworkAccessManager.instance()

    def get(self, url, **kwargs):
        if isinstance(url, str):
            url = QUrl(url)
        request = QNetworkRequest(url)
        request = self.adapter.configureRequest(request)
        return self.manager.get(request)


def getLegacySession():
    return LegacySession()


def getSync(url):
    session = getLegacySession()
    reply = session.get(url)

    loop = QEventLoop()
    reply.finished.connect(loop.quit)
    loop.exec()

    try:
        # Sprawdzenie błędu sieciowego (Qt5/Qt6)
        error_val = reply.error()
        if hasattr(QNetworkReply, 'NetworkError'):
            no_err = QNetworkReply.NetworkError.NoError
        else:
            no_err = QNetworkReply.NoError

        if error_val != no_err:
            return None

        # Sprawdzenie kodu HTTP
        if hasattr(QNetworkRequest, 'Attribute'):
            status_attr = QNetworkRequest.Attribute.HttpStatusCodeAttribute
        else:
            status_attr = QNetworkRequest.HttpStatusCodeAttribute

        status_code = reply.attribute(status_attr)
        if status_code != 200:
            return None

        # Odczyt danych (Qt5/Qt6)
        read_data = reply.readAll()
        if hasattr(read_data, 'data'):
            return read_data.data().decode('utf-8')
        return bytes(read_data).decode('utf-8')
    finally:
        reply.deleteLater()