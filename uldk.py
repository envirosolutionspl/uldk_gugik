import requests
import os
class RegionFetch:
    def __init__(self):
        self.wojewodztwoDict = self.__fetchWojewodztwoDict()
        self.powiatDict = self.__fetchPowiatDict()
        self.gminaDict = self.__fetchGminaDict()
        self.obrebDict = self.__fetchObrebDict()
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



    def __fetchGminaDict(self):
        resp = requests.get('https://uldk.gugik.gov.pl/service.php?obiekt=gmina&wynik=gmina,powiat,teryt,wojewodztwo')
        gmList = resp.text.strip().split('\n')
        gmDict = {}
        if len(gmList) and gmList[0] == '0':
            gmList = gmList[1:]
            for el in gmList:
                split = el.split('|')
                if split[0] == "Warszawa (miasto)":
                    split[2] = split[2][:-1] + "8"
                    print("Wawa: ", split[2])
                if split[0] in ["Kraków (miasto)", "Łódź (miasto)"]:
                    split[2] = split[2][:-1] + "9"
                    print("Łódź/Kraków: ", split[2])
                gmDict[split[2]] = split[0], split[1], split[3]
            return gmDict
        else:
            return {}
    def __fetchPowiatDict(self):
        resp = requests.get('https://uldk.gugik.gov.pl/service.php?obiekt=powiat&wynik=powiat,teryt,wojewodztwo')
        powList = resp.text.strip().split('\n')
        powDict = {}
        if len(powList) and powList[0] == '0':
            powList = powList[1:]
            for el in powList:
                split = el.split('|')
                powDict[split[1]] = split[0], split[2]
            return powDict
        else:
            return {}

    def __fetchWojewodztwoDict(self):
        resp = requests.get('https://uldk.gugik.gov.pl/service.php?obiekt=wojewodztwo&wynik=wojewodztwo,teryt')
        wojList = resp.text.strip().split('\n')
        wojDict = {}
        if len(wojList) and wojList[0] == '0':
            wojList = wojList[1:]
            for el in wojList:
                split = el.split('|')
                wojDict[split[0]] = split[1]
            return wojDict
        else:
            return {}

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
                temp = vG[0]
                if vG[0][-1] == "3": # 
                    for i in [1, 2, 4, 5]: 
                        temp = temp[:-1] + str(i)               
                        if temp == vO and kG == name_gmina: 
                            self.filteredObrebDict[kO] = vO, name_gmina
                else:
                    if name_gmina == "Warszawa (miasto)":
                        self.replace_id(name_gmina, temp, [2, 20], vO, kG, kO)
                    if name_gmina == "Kraków (miasto)":
                        self.replace_id(name_gmina, temp, [2, 6], vO, kG, kO)
                    if name_gmina == "Łódź (miasto)":
                        self.replace_id(name_gmina, temp, [2, 7], vO, kG, kO)
                    if temp == vO and kG == name_gmina: 
                            self.filteredObrebDict[kO] = vO, name_gmina
        return  self.filteredObrebDict
    
    
    def replace_at_idx(self, word: str, idx: list[int], to_replace: str):
        new_word = list(word)
        for i, index in enumerate(idx):
            new_word[index] = to_replace[i]
        return "".join(new_word)
    
    def replace_id(self, name_gmina: str, id: str, r: list[int], vO, kG, kO):
        g = {"Warszawa (miasto)": "8", "Kraków (miasto)": "9", "Łódź (miasto)": "9"}
        for i in range(r[0], r[1]):
            x = f"{i:02d}"
            temp = self.replace_at_idx(id, [4, 5], x)
            if temp == vO and kG == name_gmina: 
                    self.filteredObrebDict[kO] = vO, name_gmina

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