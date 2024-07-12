from .constants import DEFAULT_SRID
from .request import Request


def getParcelByXY(xy, objectType):
    request = "GetParcelByXY"
    result = "geom_wkt,teryt,parcel,region,commune,county,voivodeship"
    params = {'request': request, 'xy': xy, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, objectType)
    return res.data


def getRegionByXY(xy, objectType):
    request = "GetRegionByXY"
    result = "geom_wkt,teryt,region,commune,county,voivodeship"
    params = {'request': request, 'xy': xy, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, objectType)
    return res.data


def getCommuneByXY(xy, objectType):
    request = "GetCommuneByXY"
    result = "geom_wkt,teryt,commune,county,voivodeship"
    params = {'request': request, 'xy': xy, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, objectType)
    return res.data


def getCountyByXY(xy, objectType):
    request = "GetCountyByXY"
    result = "geom_wkt,teryt,county,voivodeship"
    params = {'request': request, 'xy': xy, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, objectType)
    return res.data


def getVoivodeshipByXY(xy, objectType):
    request = "GetVoivodeshipByXY"
    result = "geom_wkt,teryt,voivodeship"
    params = {'request': request, 'xy': xy, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, objectType)
    return res.data


def GetBuildingByXY(xy, object_type):
    request = "GetBuildingByXY"
    result = "geom_wkt,teryt"
    params = {'request': request, 'xy': xy, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, object_type)
    return res.data


