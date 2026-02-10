import json
from qgis.core import QgsMessageLog
from qgis.PyQt.QtNetwork import QNetworkReply
from qgis.PyQt.QtCore import QEventLoop

from .https_adapter import getLegacySession
from .constants import (
    REST_API_BASE_URL,
    REST_ENDPOINT_VOIVODESHIP,
    REST_ENDPOINT_COUNTY,
    REST_ENDPOINT_COMMUNE,
    REST_ENDPOINT_PRECINCT,
    LOG_TAG,
)

# Qt5/Qt6 compat
if not hasattr(QEventLoop, 'exec'):
    QEventLoop.exec = QEventLoop.exec_


class RegionFetch:
    def __init__(self, teryt):
        self.wojewodztwo_dict = self.__fetch_wojewodztwo_dict()
        self.powiat_dict = self.get_powiat_by_teryt(teryt)
        self.gmina_dict = self.get_gmina_by_teryt(teryt)
        self.obreb_dict = self.get_obreb_by_teryt(teryt)

    @staticmethod
    def fetch_unit_dict(endpoint):
        unit_dict = {}
        url = f"{REST_API_BASE_URL}{endpoint}"
        try:
            QgsMessageLog.logMessage(f"Pobieranie danych z: {url}", LOG_TAG)

            session = getLegacySession()
            reply = session.get(url)

            loop = QEventLoop()
            reply.finished.connect(loop.quit)
            loop.exec()

            # Sprawdzenie błędu (Qt5/Qt6)
            error_val = reply.error()
            if hasattr(QNetworkReply, 'NetworkError'):
                no_err = QNetworkReply.NetworkError.NoError
            else:
                no_err = QNetworkReply.NoError

            if error_val != no_err:
                QgsMessageLog.logMessage(
                    f"Błąd sieci przy pobieraniu: {url}: {reply.errorString()}", LOG_TAG
                )
                reply.deleteLater()
                return unit_dict

            # Odczyt danych (Qt5/Qt6)
            read_data = reply.readAll()
            if hasattr(read_data, 'data'):
                raw = read_data.data().decode('utf-8')
            else:
                raw = bytes(read_data).decode('utf-8')

            reply.deleteLater()

            data = json.loads(raw)
            for item in data:
                unit_dict[item['teryt']] = item['name']

        except Exception as e:
            QgsMessageLog.logMessage(
                f"Wyjątek przy pobieraniu {url}: {str(e)}", LOG_TAG
            )
        return unit_dict

    def __fetch_wojewodztwo_dict(self):
        return self.fetch_unit_dict(REST_ENDPOINT_VOIVODESHIP)

    def get_powiat_by_teryt(self, teryt):
        if not teryt:
            return {}
        return self.fetch_unit_dict(f"{REST_ENDPOINT_COUNTY}/{teryt}")

    def get_gmina_by_teryt(self, teryt):
        if not teryt:
            return {}
        return self.fetch_unit_dict(f"{REST_ENDPOINT_COMMUNE}/{teryt}")

    def get_obreb_by_teryt(self, teryt):
        if not teryt:
            return {}
        return self.fetch_unit_dict(f"{REST_ENDPOINT_PRECINCT}/{teryt}")

    # Aliasy dla dialogu (constants.ADMINISTRATIVE_UNITS_OBJECTS
    # wywołuje getPowiatByTeryt, getGminaByTeryt, getObrebByTeryt przez getattr)
    getPowiatByTeryt = get_powiat_by_teryt
    getGminaByTeryt = get_gmina_by_teryt
    getObrebByTeryt = get_obreb_by_teryt
