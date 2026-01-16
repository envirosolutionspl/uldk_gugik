from .constants import DEFAULT_SRID
from .request import Request as RQ
from .request_search import Request as RS
from .request_region import Request as RR


def getParcelById(name, object_type, **kwargs):
    request = "GetParcelByIdOrNr"
    result = "geom_wkt,teryt,parcel,region,commune,county,voivodeship"
    params = {'request': request, 'id': name, 'result': result, 'srid': DEFAULT_SRID}
    res = RQ(params, object_type, **kwargs)
    return res.data


def getParcelById2(name, **kwargs):
    request = "GetParcelByIdOrNr"
    result = "geom_wkt,teryt,parcel,region,commune,county,voivodeship"
    params = {'request': request, 'id': name, 'result': result, 'srid': DEFAULT_SRID}
    res = RS(params, **kwargs)
    return res.data


def getRegionById(id, **kwargs):
    request = "getRegionById"
    result = "teryt,region,commune,county,voivodeship"
    params = {'request': request, 'id': id, 'result': result, 'srid': DEFAULT_SRID}
    res = RR(params, **kwargs)
    return res.data
