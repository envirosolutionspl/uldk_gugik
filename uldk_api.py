from .request import Request


def getParcelById(id, srid, objectType):
    request = "GetParcelById"
    result = "geom_wkt,teryt,parcel,region,commune,county,voivodeship"
    params = {'request': request, 'id': id, 'result': result, 'srid': srid}
    res = Request(params, objectType)
    return res.data


def getRegionById(id, srid, objectType, **kwargs):
    request = "GetRegionById"
    result = "geom_wkt,teryt,region,commune,county,voivodeship"
    params = {'request': request, 'id': id, 'result': result, 'srid': srid}
    res = Request(params, objectType, **kwargs)
    return res.data


def getCommuneById(id, srid, objectType):
    request = "GetCommuneById"
    result = "geom_wkt,teryt,commune,county,voivodeship"
    params = {'request': request, 'id': id, 'result': result, 'srid': srid}
    res = Request(params, objectType)
    return res.data


def getCountyById(id, srid, objectType):
    request = "GetCountyById"
    result = "geom_wkt,teryt,county,voivodeship"
    params = {'request': request, 'id': id, 'result': result, 'srid': srid}
    res = Request(params, objectType)
    return res.data


def getVoivodeshipById(id, srid, objectType):
    request = "GetVoivodeshipById"
    result = "geom_wkt,teryt,voivodeship"
    params = {'request': request, 'id': id, 'result': result, 'srid': srid}
    res = Request(params, objectType)
    return res.data

