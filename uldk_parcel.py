from .request import Request


def getParcelById(name, srid, **kwargs):
    request = "GetParcelByIdOrNr"
    result = "geom_wkt,teryt,parcel,region,commune,county,voivodeship"
    params = {'request': request, 'id': name, 'result': result, 'srid': srid}
    res = Request(params, **kwargs)
    return res.data

