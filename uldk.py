from PyQt5.QtNetwork import QNetworkRequest, QNetworkAccessManager, QNetworkReply
from PyQt5.QtCore import QUrl, QEventLoop


class RegionFetch:
    def __init__(self):
        self.loop = QEventLoop()
        self.wojewodztwoDict = {}
        self.powiatDict = {}
        self.gminaDict = {}
        self.obrebDict = {}
        
        self.filteredPowiatDict = {}
        self.filteredGminaDict = {}
        self.filteredObrebDict = {}

        self.__fetchWojewodztwo()

    def __fetchWojewodztwo(self):
        manager = QNetworkAccessManager()
        resp = QNetworkRequest(QUrl('https://uldk.gugik.gov.pl/service.php?obiekt=wojewodztwo&wynik=nazwa%2Cteryt&teryt='))
        manager.get(resp)
        manager.finished.connect(self.getWojewodztwo)
        self.loop.exec_()
        
    def __fetchPowiat(self, woj_name):
        teryt = self.wojewodztwoDict[woj_name]
        manager = QNetworkAccessManager()
        resp = QNetworkRequest(QUrl(f'https://uldk.gugik.gov.pl/service.php?obiekt=powiat&wynik=nazwa%2Cteryt,wojewodztwo&teryt={teryt}'))
        manager.get(resp)
        manager.finished.connect(self.getPowiat)
        self.loop.exec_()
        
    def __fetchGmina(self, powiat_name):
        teryt = self.powiatDict[powiat_name][0]
        manager = QNetworkAccessManager()                   
        resp = QNetworkRequest(QUrl(f'https://uldk.gugik.gov.pl/service.php?obiekt=gmina&wynik=nazwa,powiat%2Cteryt,wojewodztwo&teryt={teryt}'))
        manager.get(resp)
        manager.finished.connect(self.getGmina)
        self.loop.exec_()
        
    def __fetchObreb(self, gmina_name):
        teryt = self.gminaDict[gmina_name][1]
        manager = QNetworkAccessManager()
        resp = QNetworkRequest(QUrl(f'https://uldk.gugik.gov.pl/service.php?obiekt=obreb&wynik=nazwa%2Cteryt&teryt={teryt}&'))
        manager.get(resp)
        manager.finished.connect(self.getObreb)
        self.loop.exec_()
        
    def getWojewodztwo(self, reply):
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll().data().decode('utf-8')
            data = data.strip().split('\n')            
            if len(data) and data[0] == '0':
                data = data[1:]
                for el in data:
                    split = el.split('|')
                    self.wojewodztwoDict[split[0]] = split[1]
        self.loop.quit()
     
    def getPowiat(self, reply):
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll().data().decode('utf-8')
            data = data.strip().split('\n')
            if len(data) and data[0] == '0':
                data = data[1:]
                self.powiatDict.clear()
                for el in data:
                    split = el.split('|')
                    # self.powiatDict[split[1]] = split[0], split[2]
                    self.powiatDict[split[0]] = split[1], split[2]
        self.loop.quit()

    def getGmina(self, reply):
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll().data().decode('utf-8')
            data = data.strip().split('\n')
            if len(data) and data[0] == '0':
                data = data[1:]
                self.gminaDict.clear()
                for el in data:
                    split = el.split('|')
                    # self.gminaDict[split[2]] = split[0], split[1], split[3]
                    self.gminaDict[split[0]] = split[1], split[2], split[3]
        self.loop.exit(0)

    def getObreb(self, reply):
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll().data().decode('utf-8')
            data = data.strip().split('\n') 
            if len(data) and data[0] == '0':
                data = data[1:]
                self.obrebDict.clear()
                for el in data:
                    split = el.split('|')
                    self.obrebDict[split[0]] = split[1]
        self.loop.quit()
        
    def getPowiatDictByWojewodztwoName(self, woj_name):
        if not woj_name:
            return {}
        self.__fetchPowiat(woj_name)
        return self.powiatDict

    def getGminaDictByPowiatName(self, name_powiat):
        if not name_powiat:
            return {}
        self.__fetchGmina(name_powiat)
        return self.gminaDict

    def getObrebDictByGminaName(self, name_gmina):
        if not name_gmina:
            return {}
        self.__fetchObreb(name_gmina)
        return  self.obrebDict


if __name__ == '__main__':
    regionFetch = RegionFetch()
    #print(regionFetch.wojewodztwoDict)
    #print(regionFetch.obrebDict)
    #print(regionFetch.getGminaDictByPowiatName('bolesławiecki'))
    #print('---------------------------')
    #print(regionFetch.getObrebDictByGminaName('Bolesławiec (miasto)'))
    #print(regionFetch.gminaDict)
    #print(regionFetch.wojDict)
    #print(regionFetch.getPowiatDictByWojewodztwoName('mazowieckie'))


    #print(regionFetch.openObrebList())
    
    # class RegionFetch:
#     def __init__(self):
#         self.wojewodztwoDict = self.__fetchWojewodztwoDict()
#         self.powiatDict = self.__fetchPowiatDict()
#         self.gminaDict = self.__fetchGminaDict()
        
#         self.filteredPowiatDict = {}
#         self.filteredGminaDict = {}
#         self.filteredObrebDict = {}

#     def openObrebList(self):
#         with open(os.path.join(os.path.dirname(__file__),'obreby.csv'), encoding="ANSI") as f:
#             resp = f.readlines()
#             resp = [w.replace('\n', '') for w in resp]
#             resp = [x[:8]+x[13:] for x in resp]

#         return resp

#     def __fetchObrebDict(self, name_gmina):
#         teryt = self.filteredGminaDict[name_gmina][0]
#         resp = requests.get(f'https://uldk.gugik.gov.pl/service.php?obiekt=obreb&wynik=nazwa%2Cteryt&teryt={teryt}&')
#         obrebList = resp.text.strip().split('\n')
#         obrebDict = {}
#         if len(obrebList) and obrebList[0] == '0':
#             obrebList = obrebList[1:]
#             for el in obrebList:
#                 split = el.split('|')
#                 obrebDict[split[0]] = split[1]
#             return obrebDict
#         else:
#             return {}

#     def __fetchGminaDict(self):
#         resp = requests.get('https://uldk.gugik.gov.pl/service.php?obiekt=gmina&wynik=gmina,powiat,teryt,wojewodztwo')
#         gmList = resp.text.strip().split('\n')
#         gmDict = {}
#         if len(gmList) and gmList[0] == '0':
#             gmList = gmList[1:]
#             for el in gmList:
#                 split = el.split('|')
#                 gmDict[split[2]] = split[0], split[1], split[3]
#             return gmDict
#         else:
#             return {}
        
#     def __fetchPowiatDict(self):
#         resp = requests.get('https://uldk.gugik.gov.pl/service.php?obiekt=powiat&wynik=powiat,teryt,wojewodztwo')
#         powList = resp.text.strip().split('\n')
#         powDict = {}
#         if len(powList) and powList[0] == '0':
#             powList = powList[1:]
#             for el in powList:
#                 split = el.split('|')
#                 powDict[split[1]] = split[0], split[2]
#             return powDict
#         else:
#             return {}

#     def __fetchWojewodztwoDict(self):
#         resp = requests.get('https://uldk.gugik.gov.pl/service.php?obiekt=wojewodztwo&wynik=wojewodztwo,teryt')
#         wojList = resp.text.strip().split('\n')
#         wojDict = {}
#         if len(wojList) and wojList[0] == '0':
#             wojList = wojList[1:]
#             for el in wojList:
#                 split = el.split('|')
#                 wojDict[split[0]] = split[1]
#             return wojDict
#         else:
#             return {}

#     def getPowiatDictByWojewodztwoName(self, name):
#         self.filteredPowiatDict = {}
#         for k, v in self.powiatDict.items():
#             if v[1] == name:
#                 self.filteredPowiatDict[v[0]] = k, name

#         return self.filteredPowiatDict

#     def getGminaDictByPowiatName(self, name_powiat):
#         self.filteredGminaDict = {}
#         for k, v in self.gminaDict.items():
#             if v[1] == name_powiat:
#                 self.filteredGminaDict[v[0]] = k, name_powiat
#         return self.filteredGminaDict

#     def getObrebDictByGminaName(self, name_gmina):
#         if name_gmina == "":
#             return {}
#         self.obrebDict = self.__fetchObrebDict(name_gmina)
#         return  self.obrebDict
