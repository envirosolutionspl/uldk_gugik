from .constants import ULDK_GMINA_DICT_URL, ULDK_POWIAT_DICT_URL, ULDK_WOJEWODZTWO_DICT_URL, ULDK_OBREB_DICT_URL
from .https_adapter import getLegacySession


class RegionFetch:
    def __init__(self, teryt):
        self.wojewodztwo_dict = self.__fetchWojewodztwoDict(teryt = '')
        self.powiat_dict = self.getPowiatByTeryt(teryt)
        self.gmina_dict = self.getGminaByTeryt(teryt)
        self.obreb_dict = self.getObrebByTeryt(teryt)

    @staticmethod
    def fetchUnitDict(url, teryt):
        unit_dict = {}
        url = url+teryt
        with getLegacySession().get(url=url, verify=False) as resp:
            resp_text = resp.text.strip().split('\n')
            if not resp_text:
                return
            for el in resp_text[1:]:
                split = el.split('|')
                unit_dict[split[1]] = split[0]
        return unit_dict

    def __fetchWojewodztwoDict(self, teryt):
        return self.fetchUnitDict(ULDK_WOJEWODZTWO_DICT_URL, teryt='')

    def getPowiatByTeryt(self, teryt):
        return self.fetchUnitDict(ULDK_POWIAT_DICT_URL, teryt)  

    def getGminaByTeryt(self, teryt):
        return self.fetchUnitDict(ULDK_GMINA_DICT_URL, teryt)

    def getObrebByTeryt(self, teryt):
        return self.fetchUnitDict(ULDK_OBREB_DICT_URL, teryt)


# if __name__ == '__main__':
#     region_fetch = region_fetch(teryt)
