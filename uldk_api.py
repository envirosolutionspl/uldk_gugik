from .request import Request


def getParcelById(id, srid):
    request = "GetParcelById"
    result = "geom_wkt,teryt,parcel,region,commune,county,voivodeship"
    params = {'request': request, 'id': id, 'result': result, 'srid': srid}
    res = Request(params)
    return res.data
    

# def getBuildingById(id, srid):
#     request = "GetBuildingById"
#     result = "geom_wkt,region,commune,county,voivodeship"
#     params = {'request': request, 'id': id, 'result': result, 'srid': srid}
#     res = Request(params)
#     return res.data


def getRegionById(id, srid, **kwargs):
    request = "GetRegionById"
    result = "geom_wkt,teryt,region,commune,county,voivodeship"
    params = {'request': request, 'id': id, 'result': result, 'srid': srid}
    res = Request(params, **kwargs)
    return res.data


def getCommuneById(id, srid):
    request = "GetCommuneById"
    result = "geom_wkt,teryt,commune,county,voivodeship"
    params = {'request': request, 'id': id, 'result': result, 'srid': srid}
    res = Request(params)
    return res.data


def getCountyById(id, srid):
    request = "GetCountyById"
    result = "geom_wkt,teryt,county,voivodeship"
    params = {'request': request, 'id': id, 'result': result, 'srid': srid}
    res = Request(params)
    return res.data


def getVoivodeshipById(id, srid):
    request = "GetVoivodeshipById"
    result = "geom_wkt,teryt,voivodeship"
    params = {'request': request, 'id': id, 'result': result, 'srid': srid}
    res = Request(params)
    return res.data

