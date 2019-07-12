import requests
from qgis.core import QgsVectorLayer, QgsGeometry, QgsFeature, QgsProject

URL = "http://uldk.gugik.gov.pl/"

def getRequest(id, request):
    PARAMS = {'request': request, 'id': id, 'result': 'geom_wkt'}
    r = requests.get(url=URL, params=PARAMS)
    r_txt = r.text
    if r.status_code == 200 and r_txt[0] == '0':
        if ";" in r_txt:
            return r_txt.split('\n')[1].split(';')[1]
        else:
            return r_txt.split('\n')[1]
    else:
        print(r_txt)
        return None

def getParcelById(id):
    request = "GetParcelById"
    return getRequest(id,request)

def getRegionById(id):
    request = "GetRegionById"
    return getRequest(id,request)

def getCommuneById(id):
    request = "GetCommuneById"
    return getRequest(id,request)

def getCountyById(id):
    request = "GetCountyById"
    return getRequest(id,request)

def getVoivodeshipById(id):
    request = "GetVoivodeshipById"
    return getRequest(id,request)