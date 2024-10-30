from . constants import DEFAULT_SRID
from .request import Request


def getBuildingById(id, object_type):
    request = "GetBuildingById"
    result = "geom_wkt,teryt,region,commune,county,voivodeship"
    params = {'request': request, 'id': id, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, object_type)
    return res.data

def getParcelById(id, objectType):
    request = "GetParcelById"
    result = "geom_wkt,teryt,parcel,region,commune,county,voivodeship"
    params = {'request': request, 'id': id, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, objectType)
    return res.data


def getRegionById(id, objectType, **kwargs):
    request = "GetRegionById"
    result = "geom_wkt,teryt,region,commune,county,voivodeship"
    params = {'request': request, 'id': id, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, objectType, **kwargs)
    return res.data


def getCommuneById(id, objectType):
    request = "GetCommuneById"
    result = "geom_wkt,teryt,commune,county,voivodeship"
    params = {'request': request, 'id': id, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, objectType)
    return res.data


def getCountyById(id, objectType):
    request = "GetCountyById"
    result = "geom_wkt,teryt,county,voivodeship"
    params = {'request': request, 'id': id, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, objectType)
    return res.data


def getVoivodeshipById(id, objectType):
    request = "GetVoivodeshipById"
    result = "geom_wkt,teryt,voivodeship"
    params = {'request': request, 'id': id, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, objectType)
    return res.data
