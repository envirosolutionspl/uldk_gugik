import json
from qgis.core import QgsMessageLog

from .https_adapter import NetworkManager
from .constants import (
    REST_API_BASE_URL,
    REST_ENDPOINT_VOIVODESHIP,
    REST_ENDPOINT_COUNTY,
    REST_ENDPOINT_COMMUNE,
    REST_ENDPOINT_PRECINCT,
    LOG_TAG,
)


class RegionFetch:
    def __init__(self, teryt):
        self.manager = NetworkManager()
        self.wojewodztwo_dict = self.__fetch_wojewodztwo_dict()
        self.powiat_dict = self.get_powiat_by_teryt(teryt)
        self.gmina_dict = self.get_gmina_by_teryt(teryt)
        self.obreb_dict = self.get_obreb_by_teryt(teryt)

    def fetch_unit_dict(self, endpoint):
        unit_dict = {}
        url = f"{REST_API_BASE_URL}{endpoint}"
        try:
            QgsMessageLog.logMessage(f"Pobieranie danych z: {url}", LOG_TAG)
            raw = self.manager.getSync(url)
            if raw is None:
                QgsMessageLog.logMessage(
                    f"Błąd sieci przy pobieraniu: {url}", LOG_TAG
                )
                return unit_dict
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
