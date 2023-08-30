from .request import Request


def getParcelById(name, srid):
    request = "GetParcelByIdOrNr"
    result = "geom_wkt,teryt,parcel,region,commune,county,voivodeship"
    params = {'request': request, 'id': name, 'result': result, 'srid': srid}
    res = Request(params)
    return res.data

