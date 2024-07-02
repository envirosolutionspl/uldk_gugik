from .utils import default_srid
from .request import Request as RQ
from .request_search import Request as RS
from .request_region import Request as RR


def getParcelById(name, objectType, **kwargs):
    request = "GetParcelByIdOrNr"
    result = "geom_wkt,teryt,parcel,region,commune,county,voivodeship"
    params = {'request': request, 'id': name, 'result': result, 'srid': default_srid}
    res = RQ(params, objectType, **kwargs)
    return res.data


def getParcelById2(name, **kwargs):
    request = "GetParcelByIdOrNr"
    result = "geom_wkt,teryt,parcel,region,commune,county,voivodeship"
    params = {'request': request, 'id': name, 'result': result, 'srid': default_srid}
    res = RS(params, **kwargs)
    return res.data


def GetRegionById(id, **kwargs):
    request = "GetRegionById"
    result = "teryt,region,commune,county,voivodeship"
    params = {'request': request, 'id': id, 'result': result, 'srid': default_srid}
    res = RR(params, **kwargs)
    return res.data
