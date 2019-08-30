import requests
from qgis.core import QgsVectorLayer, QgsGeometry, QgsFeature, QgsProject
from . import uldk_teryt

URL = "http://uldk.gugik.gov.pl/"


def getRequestXY(xy, request, result, srid):
    PARAMS = {'request': request, 'xy': xy, 'result': result, 'srid': srid}
    r = requests.get(url=URL, params=PARAMS)
    r_txt = r.text
    #print(r_txt)
    if r.status_code == 200 and r_txt[0] == '0':
        if ";" in r_txt:
            return r_txt.split('\n')[1].split(';')[1]
        else:
            return r_txt.split('\n')[1]
    else:
        print(r_txt)
        return None


def getParcelByXY(xy, srid):
    request = "GetParcelByXY"
    result = "geom_wkt,teryt,parcel,region,commune,county,voivodeship"
    return getRequestXY(xy, request, result, srid)


def getRegionByXY(xy, srid):
    request = "GetRegionByXY"
    result = "geom_wkt,teryt,region,commune,county,voivodeship"
    return getRequestXY(xy, request, result, srid)


def getCommuneByXY(xy, srid):
    request = "GetCommuneByXY"
    result = "geom_wkt,teryt,commune,county,voivodeship"
    return getRequestXY(xy, request, result, srid)


def getCountyByXY(xy, srid):
    request = "GetCountyByXY"
    result = "geom_wkt,teryt,county,voivodeship"
    return getRequestXY(xy, request, result, srid)


def getVoivodeshipByXY(xy, srid):
    request = "GetVoivodeshipByXY"
    result = "geom_wkt,teryt,voivodeship"
    return getRequestXY(xy, request, result, srid)
