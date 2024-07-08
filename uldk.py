from .constants import ULDK_GMINA_DICT_URL, ULDK_POWIAT_DICT_URL, ULDK_WOJEWODZTWO_DICT_URL, ULDK_OBREB_DICT_URL
from .https_adapter import get_legacy_session


class RegionFetch:
    def __init__(self):
        self.wojewodztwo_dict = self.__fetch_wojewodztwo_dict()
        self.powiat_dict = self.__fetch_powiat_dict()
        self.gmina_dict = self.__fetch_gmina_dict()

    @staticmethod
    def fetch_unit_dict(url):
        unit_dict = {}
        with get_legacy_session().get(url=url, verify=False) as resp:
            resp_text = resp.text.strip().split('\n')
            if not resp_text:
                return
            for el in resp_text[1:]:
                split = el.split('|')
                unit_dict[split[1]] = split[0]
        return unit_dict

    def __fetch_obreb_dict(self):
        return self.fetch_unit_dict(ULDK_OBREB_DICT_URL)

    def __fetch_gmina_dict(self):
        return self.fetch_unit_dict(ULDK_GMINA_DICT_URL)

    def __fetch_powiat_dict(self):
        return self.fetch_unit_dict(ULDK_POWIAT_DICT_URL)

    def __fetch_wojewodztwo_dict(self):
        return self.fetch_unit_dict(ULDK_WOJEWODZTWO_DICT_URL)

    def get_powiat_by_teryt(self, teryt):
        return {key: val for key, val in self.powiat_dict.items() if key.startswith(teryt)}

    def get_gmina_by_teryt(self, teryt):
        return {key: val for key, val in self.gmina_dict.items() if key.startswith(teryt)}

    def get_obreb_by_teryt(self, teryt):
        return {key: val for key, val in self.gmina_dict.items() if key.startswith(teryt)}


if __name__ == '__main__':
    regionFetch = RegionFetch()
