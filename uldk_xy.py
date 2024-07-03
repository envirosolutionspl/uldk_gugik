from urllib.parse import urlencode
from qgis.core import QgsVectorLayer, QgsGeometry, QgsFeature, QgsProject

from .request import Request

from . import uldk_teryt


def getParcelByXY(xy, srid, objectType):
    request = "GetParcelByXY"
    result = "geom_wkt,teryt,parcel,region,commune,county,voivodeship"
    params = {'request': request, 'xy': xy, 'result': result, 'srid': srid}
    res = Request(params,objectType)
    return res.data
    
def getRegionByXY(xy, srid, objectType):
    request = "GetRegionByXY"
    result = "geom_wkt,teryt,region,commune,county,voivodeship"
    params = {'request': request, 'xy': xy, 'result': result, 'srid': srid}
    res = Request(params,objectType)
    return res.data


def getCommuneByXY(xy, srid, objectType):
    request = "GetCommuneByXY"
    result = "geom_wkt,teryt,commune,county,voivodeship"
    params = {'request': request, 'xy': xy, 'result': result, 'srid': srid}
    res = Request(params,objectType)
    return res.data


def getCountyByXY(xy, srid, objectType):
    request = "GetCountyByXY"
    result = "geom_wkt,teryt,county,voivodeship"
    params = {'request': request, 'xy': xy, 'result': result, 'srid': srid}
    res = Request(params,objectType)
    return res.data


def getVoivodeshipByXY(xy, srid, objectType):
    request = "GetVoivodeshipByXY"
    result = "geom_wkt,teryt,voivodeship"
    params = {'request': request, 'xy': xy, 'result': result, 'srid': srid}
    res = Request(params,objectType)
    return res.data
