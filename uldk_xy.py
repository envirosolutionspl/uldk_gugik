from urllib.parse import urlencode
from qgis.core import QgsVectorLayer, QgsGeometry, QgsFeature, QgsProject

from .request import Request

from . import uldk_teryt


def getParcelByXY(xy, srid):
    request = "GetParcelByXY"
    result = "geom_wkt,teryt,parcel,region,commune,county,voivodeship"
    params = {'request': request, 'xy': xy, 'result': result, 'srid': srid}
    res = Request(params)
    return res.data

def getBuildingByXY(xy, srid):
    request = "GetBuildingByXY"
    result = "geom_wkt,region,commune,county,voivodeship"
    params = {'request': request, 'xy': xy, 'result': result, 'srid': srid}
    res = Request(params)
    return res.data
    
def getRegionByXY(xy, srid):
    request = "GetRegionByXY"
    result = "geom_wkt,teryt,region,commune,county,voivodeship"
    params = {'request': request, 'xy': xy, 'result': result, 'srid': srid}
    res = Request(params)
    return res.data


def getCommuneByXY(xy, srid):
    request = "GetCommuneByXY"
    result = "geom_wkt,teryt,commune,county,voivodeship"
    params = {'request': request, 'xy': xy, 'result': result, 'srid': srid}
    res = Request(params)
    return res.data


def getCountyByXY(xy, srid):
    request = "GetCountyByXY"
    result = "geom_wkt,teryt,county,voivodeship"
    params = {'request': request, 'xy': xy, 'result': result, 'srid': srid}
    res = Request(params)
    return res.data


def getVoivodeshipByXY(xy, srid):
    request = "GetVoivodeshipByXY"
    result = "geom_wkt,teryt,voivodeship"
    params = {'request': request, 'xy': xy, 'result': result, 'srid': srid}
    res = Request(params)
    return res.data
