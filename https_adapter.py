import warnings
import ssl

from qgis.core import QgsNetworkAccessManager
from qgis.PyQt.QtNetwork import QNetworkRequest, QSslConfiguration, QSslSocket
from qgis.PyQt.QtCore import QUrl


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