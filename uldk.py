from .constants import ULDK_GMINA_DICT_URL, ULDK_POWIAT_DICT_URL, ULDK_WOJEWODZTWO_DICT_URL, ULDK_OBREB_DICT_URL
from qgis.PyQt.QtCore import QUrl, QUrlQuery, QEventLoop
from qgis.PyQt.QtNetwork import QNetworkReply
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
        session = getLegacySession()
        reply = session.get(url)
        loop = QEventLoop()
        
        def handleReply():
            error_val = reply.error()
            if hasattr(QNetworkReply, 'NetworkError'):
                no_err = QNetworkReply.NetworkError.NoError  # Qt6
                is_no_error = (error_val == no_err)  # W Qt6 porównujemy enumy bezpośrednio
            else:
                no_err = QNetworkReply.NoError  # Qt5
                is_no_error = (int(error_val) == int(no_err))  # W Qt5 konwertujemy na int
            
            if is_no_error:
                read_data = reply.readAll()
                if hasattr(read_data, 'data'):
                    data = read_data.data().decode("utf-8")
                else:
                    data = bytes(read_data).decode("utf-8")
                resp_text = data.strip().split('\n')
                if resp_text:
                    for el in resp_text[1:]:
                        split = el.split('|')
                        if len(split) >= 2:
                            unit_dict[split[1]] = split[0]
            reply.deleteLater()
            if loop.isRunning():
                loop.quit()
        
        reply.finished.connect(handleReply)
        loop.exec()
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
