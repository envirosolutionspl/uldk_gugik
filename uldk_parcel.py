from .constants import (
    DEFAULT_SRID,
    PARCEL_BY_ID_OR_NR, REQ_REGION_BY_ID, RES_REGION_META,
)
from .request import Request as RQ
from .request_search import Request as RS
from .request_region import Request as RR


def getParcelById(name, objectType, **kwargs):
    params = {
        'request': PARCEL_BY_ID_OR_NR["request"],
        'id': name,
        'result': PARCEL_BY_ID_OR_NR["result"],
        'srid': DEFAULT_SRID
    }
    res = RQ(params, objectType, **kwargs)
    return res.data


def getParcelById2(name, **kwargs):
    params = {
        'request': PARCEL_BY_ID_OR_NR["request"],
        'id': name,
        'result': PARCEL_BY_ID_OR_NR["result"],
        'srid': DEFAULT_SRID
    }
    res = RS(params, **kwargs)
    return res.data


def GetRegionById(id, **kwargs):
    request = REQ_REGION_BY_ID
    result = RES_REGION_META
    params = {'request': request, 'id': id, 'result': result, 'srid': DEFAULT_SRID}
    res = RR(params, **kwargs)
    return res.data
