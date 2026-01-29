from .constants import (
    DEFAULT_SRID,
    REQ_BUILDING_BY_XY, REQ_PARCEL_BY_XY, REQ_REGION_BY_XY, REQ_COMMUNE_BY_XY, REQ_COUNTY_BY_XY, REQ_VOIVODESHIP_BY_XY,
    RES_BUILDING_BY_XY, RES_PARCEL_BY_XY, RES_REGION_BY_XY, RES_COMMUNE_BY_XY, RES_COUNTY_BY_XY, RES_VOIVODESHIP_BY_XY,
)
from .request import Request


def getBuildingByXY(xy, object_type):
    request = REQ_BUILDING_BY_XY
    result = ",".join(RES_BUILDING_BY_XY)
    params = {'request': request, 'xy': xy, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, object_type)
    return res.data


def getParcelByXY(xy, objectType):
    request = REQ_PARCEL_BY_XY
    result = ",".join(RES_PARCEL_BY_XY)
    params = {'request': request, 'xy': xy, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, objectType)
    return res.data


def getRegionByXY(xy, object_type):
    request = REQ_REGION_BY_XY
    result = ",".join(RES_REGION_BY_XY)
    params = {'request': request, 'xy': xy, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, object_type)
    return res.data


def getCommuneByXY(xy, object_type):
    request = REQ_COMMUNE_BY_XY
    result = ",".join(RES_COMMUNE_BY_XY)
    params = {'request': request, 'xy': xy, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, object_type)
    return res.data


def getCountyByXY(xy, object_type):
    request = REQ_COUNTY_BY_XY
    result = ",".join(RES_COUNTY_BY_XY)
    params = {'request': request, 'xy': xy, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, object_type)
    return res.data


def getVoivodeshipByXY(xy, object_type):
    request = REQ_VOIVODESHIP_BY_XY
    result = ",".join(RES_VOIVODESHIP_BY_XY)
    params = {'request': request, 'xy': xy, 'result': result, 'srid': DEFAULT_SRID}
    res = Request(params, object_type)
    return res.data
