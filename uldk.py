import os

from PyQt5.QtNetwork import QNetworkRequest, QNetworkAccessManager, QNetworkReply
from PyQt5.QtCore import QUrl, QEventLoop

class RegionFetch:
    def __init__(self):
        self.wojManager = QNetworkAccessManager()
        self.powManager = QNetworkAccessManager()
        self.gminaManager = QNetworkAccessManager()
        self.wojewodztwoDict = {}
        self.powiatDict = {}
        self.gminaDict = {}
        self.obrebDict = self.__fetchObrebDict()
        self.pendingRequest = []
        
        self.__fetchWojewodztwoDict()
        self.__fetchPowiatDict()
        self.__fetchGminaDict()
        
        self.activeRequests = 3
        self.executePendingRequest()
        self.loop = QEventLoop()
        self.loop.exec_()
        
        self.filteredPowiatDict = {}
        self.filteredGminaDict = {}
        self.filteredObrebDict = {}
            
    def openObrebList(self):
        with open(os.path.join(os.path.dirname(__file__),'obreby.csv'), encoding="ANSI") as f:
            resp = f.readlines()
            resp = [w.replace('\n', '') for w in resp]
            resp = [x[:8]+x[13:] for x in resp]

        return resp

    def __fetchObrebDict(self):
        resp=RegionFetch.openObrebList(self)
        obList = resp
        obDict = {}
        if len(obList):
            for el in obList:
                split = el.split(';')
                obDict[split[1]] = split[0]
            return obDict
        else:
            return {}

    def __fetchWojewodztwoDict(self):
        req = QNetworkRequest(QUrl('https://uldk.gugik.gov.pl/service.php?obiekt=wojewodztwo&wynik=wojewodztwo,teryt'))    
        self.pendingRequest.append((1, req))
    
    def __fetchPowiatDict(self):
        req = QNetworkRequest(QUrl('https://uldk.gugik.gov.pl/service.php?obiekt=powiat&wynik=powiat,teryt,wojewodztwo'))
        self.pendingRequest.append((2, req))
        
    def __fetchGminaDict(self):
        req = QNetworkRequest(QUrl('https://uldk.gugik.gov.pl/service.php?obiekt=gmina&wynik=gmina,powiat,teryt,wojewodztwo'))
        self.pendingRequest.append((3, req))
    
    def handleWoj(self, reply):
        """Przygotowanie danych o województwach"""
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll().data().decode('utf-8')
            data = data.strip().split('\n')            
            if len(data) and data[0] == '0':
                data = data[1:]
                for el in data:
                    split = el.split('|')
                    self.wojewodztwoDict[split[0]] = split[1]
        self.activeRequests -= 1
        if self.activeRequests == 0:
            self.loop.quit()
        
    def handlePow(self, reply):
        """Przygotowanie danych o powiatach"""
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll().data().decode('utf-8')
            data = data.strip().split('\n')
            if len(data) and data[0] == '0':
                data = data[1:]
                for el in data:
                    split = el.split('|')
                    self.powiatDict[split[1]] = split[0], split[2]
        self.activeRequests -= 1
        if self.activeRequests == 0:
            self.loop.quit()
     
    def handleGmin(self, reply):
        """Przygotowanie danych o gmianach"""
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll().data().decode('utf-8')
            data = data.strip().split('\n')
            if len(data) and data[0] == '0':
                data = data[1:]
                for el in data:
                    split = el.split('|')
                    self.gminaDict[split[2]] = split[0], split[1], split[3]
        self.activeRequests -= 1
        if self.activeRequests == 0:
            self.loop.quit()
            
    def executePendingRequest(self):
        """Obsłużenie odpowiedzi z zapytań requests"""
        managers = {
            1: (self.wojManager, self.handleWoj), 
            2: (self.powManager, self.handlePow), 
            3: (self.gminaManager, self.handleGmin)
        }
        for idx, request in self.pendingRequest:
            managers[idx][0].get(request)                       # self.wojManager.get(request)
            managers[idx][0].finished.connect(managers[idx][1]) # self.wojManger.funished.connect(self.handleWoj)
            

    def getPowiatDictByWojewodztwoName(self, name):
        self.filteredPowiatDict = {}
        for k, v in self.powiatDict.items():
            if v[1] == name:
                self.filteredPowiatDict[v[0]] = k, name

        return self.filteredPowiatDict

    def getGminaDictByPowiatName(self, name_powiat):
        self.filteredGminaDict = {}
        for k, v in self.gminaDict.items():
            if v[1] == name_powiat:
                self.filteredGminaDict[v[0]] = k, name_powiat
        return self.filteredGminaDict

    def getObrebDictByGminaName(self, name_gmina):
        self.filteredObrebDict = {}
        for kG, vG in self.filteredGminaDict.items():
            for kO, vO in self.obrebDict.items():
                if vG[0] == vO and kG == name_gmina:
                    self.filteredObrebDict[kO] = vO, name_gmina
        return  self.filteredObrebDict

if __name__ == '__main__':
    # app = QtCore.QCoreApplication([])
    regionFetch = RegionFetch()
    # app.exec_()
    #print(regionFetch.wojewodztwoDict)
    #print(regionFetch.obrebDict)
    #print(regionFetch.getGminaDictByPowiatName('bolesławiecki'))
    #print('---------------------------')
    #print(regionFetch.getObrebDictByGminaName('Bolesławiec (miasto)'))
    #print(regionFetch.gminaDict)
    #print(regionFetch.wojDict)
    #print(regionFetch.getPowiatDictByWojewodztwoName('mazowieckie'))


    #print(regionFetch.openObrebList())