from . constants import DEFAULT_SRID
from .request import Request


def getBuildingById(id, object_type):
    request = "GetBuildingById"
    result = "geom_wkt,teryt,region,commune,county,voivodeship"
    params = {'request': request, 'id': id, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, object_type)
    return res.data

def getParcelById(id, object_type):
    request = "GetParcelById"
    result = "geom_wkt,teryt,parcel,region,commune,county,voivodeship"
    params = {'request': request, 'id': id, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, object_type)
    return res.data


def getRegionById(id, object_type, **kwargs):
    request = "getRegionById"
    result = "geom_wkt,teryt,region,commune,county,voivodeship"
    params = {'request': request, 'id': id, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, object_type, **kwargs)
    return res.data


def getCommuneById(id, object_type):
    request = "GetCommuneById"
    result = "geom_wkt,teryt,commune,county,voivodeship"
    params = {'request': request, 'id': id, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, object_type)
    return res.data


def getCountyById(id, object_type):
    request = "GetCountyById"
    result = "geom_wkt,teryt,county,voivodeship"
    params = {'request': request, 'id': id, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, object_type)
    return res.data


def getVoivodeshipById(id, object_type):
    request = "GetVoivodeshipById"
    result = "geom_wkt,teryt,voivodeship"
    params = {'request': request, 'id': id, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, object_type)
    return res.data
