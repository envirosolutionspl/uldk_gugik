from urllib.parse import urlencode
from qgis.core import QgsVectorLayer, QgsGeometry, QgsFeature, QgsProject
from qgis.PyQt.QtNetwork import QNetworkReply
from qgis.PyQt.QtCore import QEventLoop

from .https_adapter import LegacySession
from .constants import ULDK_BASE_URL, ULDK_RESULT_TERYT

# Qt5/Qt6 compat: QEventLoop.exec_ -> exec
if not hasattr(QEventLoop, 'exec'):
    QEventLoop.exec = QEventLoop.exec_


def getRequestTeryt(xy, request):
    def handleReply(reply):
        nonlocal result
        nonlocal loop
        try:
            error_val = reply.error()
            if hasattr(QNetworkReply, 'NetworkError'):
                no_err = QNetworkReply.NetworkError.NoError  # Qt6
                is_no_error = (error_val == no_err)
            else:
                no_err = QNetworkReply.NoError  # Qt5
                is_no_error = (int(error_val) == int(no_err))

            if not is_no_error:
                result = None
                return

            # Odczyt danych (Qt5/Qt6)
            read_data = reply.readAll()
            if hasattr(read_data, 'data'):
                data = read_data.data().decode('utf-8')
            else:
                data = bytes(read_data).decode('utf-8')

            if not data or len(data) == 0:
                result = None
                return

            if data[0] != '0':
                result = None
                return

            lines = data.split('\n')
            if len(lines) < 2:
                result = None
                return

            second_line = lines[1]
            if ";" in second_line:
                result = second_line.split(';')[1]
            else:
                result = second_line

        except Exception:
            result = None
        finally:
            if loop.isRunning():
                loop.quit()
            reply.deleteLater()

    PARAMS = {'request': request, 'xy': xy, 'result': ULDK_RESULT_TERYT}
    url = ULDK_BASE_URL + "?" + urlencode(PARAMS)

    result = None
    session = LegacySession()
    reply = session.get(url)

    # Utworzenie loop PRZED połączeniem callback
    loop = QEventLoop()
    reply.finished.connect(lambda: handleReply(reply))
    loop.exec()

    return result
