from . constants import (
    DEFAULT_SRID,
    REQ_BUILDING_BY_ID, REQ_PARCEL_BY_ID, REQ_REGION_BY_ID, REQ_COMMUNE_BY_ID, REQ_COUNTY_BY_ID, REQ_VOIVODESHIP_BY_ID,
    RES_BUILDING_BY_ID, RES_PARCEL_BY_ID, RES_REGION_BY_ID, RES_COMMUNE_BY_ID, RES_COUNTY_BY_ID, RES_VOIVODESHIP_BY_ID
)
from .request import Request


def getBuildingById(id, object_type):
    request = REQ_BUILDING_BY_ID
    result = ",".join(RES_BUILDING_BY_ID)
    params = {'request': request, 'id': id, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, object_type)
    return res.data

def getParcelById(id, object_type):
    request = REQ_PARCEL_BY_ID
    result = ",".join(RES_PARCEL_BY_ID)
    params = {'request': request, 'id': id, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, object_type)
    return res.data


def getRegionById(id, object_type, **kwargs):
    request = REQ_REGION_BY_ID
    result = ",".join(RES_REGION_BY_ID)
    params = {'request': request, 'id': id, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, object_type, **kwargs)
    return res.data


def getCommuneById(id, object_type):
    request = REQ_COMMUNE_BY_ID
    result = ",".join(RES_COMMUNE_BY_ID)
    params = {'request': request, 'id': id, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, object_type)
    return res.data


def getCountyById(id, object_type):
    request = REQ_COUNTY_BY_ID
    result = ",".join(RES_COUNTY_BY_ID)
    params = {'request': request, 'id': id, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, object_type)
    return res.data


def getVoivodeshipById(id, object_type):
    request = REQ_VOIVODESHIP_BY_ID
    result = ",".join(RES_VOIVODESHIP_BY_ID)
    params = {'request': request, 'id': id, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, object_type)
    return res.data
