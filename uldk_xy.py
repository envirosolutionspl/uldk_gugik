import requests
from qgis.core import QgsVectorLayer, QgsGeometry, QgsFeature, QgsProject
from . import uldk_teryt

URL = "http://uldk.gugik.gov.pl/"


def getRequestXY(xy, request):
    PARAMS = {'request': request, 'xy': xy, 'result': 'geom_wkt'}
    r = requests.get(url=URL, params=PARAMS)
    r_txt = r.text

    res = ['', '']
    if r.status_code == 200 and r_txt[0] == '0':
        print(r_txt)
        if ";" in r_txt:
            res[0] = r_txt.split('\n')[1].split(';')[1]
        else:
            res[0] = r_txt.split('\n')[1]

        res[1] = uldk_teryt.getRequestTeryt(xy, request)
        return res
    else:
        print(r_txt)
        return None


def getParcelByXY(xy):
    request = "GetParcelByXY"
    return getRequestXY(xy, request)


def getRegionByXY(xy):
    request = "GetRegionByXY"
    return getRequestXY(xy, request)


def getCommuneByXY(xy):
    request = "GetCommuneByXY"
    return getRequestXY(xy, request)


def getCountyByXY(xy):
    request = "GetCountyByXY"
    return getRequestXY(xy, request)


def getVoivodeshipByXY(xy):
    request = "GetVoivodeshipByXY"
    return getRequestXY(xy, request)