from .constants import (
    DEFAULT_SRID,
    REQ_PARCEL_BY_ID_OR_NR, RES_PARCEL_BY_ID_OR_NR, REQ_REGION_BY_ID, RES_REGION_META,
)
from .request import Request as RQ
from .request_search import Request as RS
from .request_region import Request as RR


def getParcelById(name, object_type, **kwargs):
    request = REQ_PARCEL_BY_ID_OR_NR
    result = RES_PARCEL_BY_ID_OR_NR
    params = {'request': request, 'id': name, 'result': result, 'srid': DEFAULT_SRID}
    res = RQ(params, object_type, **kwargs)
    return res.data


def getParcelById2(name, **kwargs):
    request = REQ_PARCEL_BY_ID_OR_NR
    result = RES_PARCEL_BY_ID_OR_NR
    params = {'request': request, 'id': name, 'result': result, 'srid': DEFAULT_SRID}
    res = RS(params, **kwargs)
    return res.data


def GetRegionById(id, **kwargs):
    request = REQ_REGION_BY_ID
    result = RES_REGION_META
    params = {'request': request, 'id': id, 'result': result, 'srid': DEFAULT_SRID}
    res = RR(params, **kwargs)
    return res.data
