from .constants import DEFAULT_SRID
from .request import Request


def getBuildingByXY(xy, object_type):
    request = "getBuildingByXY"
    result = "geom_wkt,teryt,region,commune,county,voivodeship"
    params = {'request': request, 'xy': xy, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, object_type)
    return res.data


def getParcelByXY(xy, object_type):
    request = "GetParcelByXY"
    result = "geom_wkt,teryt,parcel,region,commune,county,voivodeship"
    params = {'request': request, 'xy': xy, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, object_type)
    return res.data


def getRegionByXY(xy, object_type):
    request = "GetRegionByXY"
    result = "geom_wkt,teryt,region,commune,county,voivodeship"
    params = {'request': request, 'xy': xy, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, object_type)
    return res.data


def getCommuneByXY(xy, object_type):
    request = "GetCommuneByXY"
    result = "geom_wkt,teryt,commune,county,voivodeship"
    params = {'request': request, 'xy': xy, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, object_type)
    return res.data


def getCountyByXY(xy, object_type):
    request = "GetCountyByXY"
    result = "geom_wkt,teryt,county,voivodeship"
    params = {'request': request, 'xy': xy, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, object_type)
    return res.data


def getVoivodeshipByXY(xy, object_type):
    request = "GetVoivodeshipByXY"
    result = "geom_wkt,teryt,voivodeship"
    params = {'request': request, 'xy': xy, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, object_type)
    return res.data
