import requests

URL = "http://uldk.gugik.gov.pl/"


def getRequest(id, request, result, srid):
    PARAMS = {'request': request, 'id': id, 'result': result, 'srid': srid}
    r = requests.get(url=URL, params=PARAMS)
    r_txt = r.text
    print(r)
    print(r_txt)
    if r.status_code == 200 and r_txt[0] == '0':
        if ";" in r_txt:
            return r_txt.split('\n')[1].split(';')[1]
        else:
            return r_txt.split('\n')[1]
    else:
        return None


def getParcelById(id, srid):
    request = "GetParcelById"
    result = "geom_wkt,teryt,parcel,region,commune,county,voivodeship"
    return getRequest(id, request, result, srid)
    
def getBuildingById(id, srid):
    request = "GetBuildingById"
    result = "geom_wkt,region,commune,county,voivodeship"
    return getRequest(id, request, result, srid)


def getRegionById(id, srid):
    request = "GetRegionById"
    result = "geom_wkt,teryt,region,commune,county,voivodeship"
    return getRequest(id, request, result, srid)


def getCommuneById(id, srid):
    request = "GetCommuneById"
    result = "geom_wkt,teryt,commune,county,voivodeship"
    return getRequest(id, request, result, srid)


def getCountyById(id, srid):
    request = "GetCountyById"
    result = "geom_wkt,teryt,county,voivodeship"
    return getRequest(id, request, result, srid)


def getVoivodeshipById(id, srid):
    request = "GetVoivodeshipById"
    result = "geom_wkt,teryt,voivodeship"
    return getRequest(id, request, result, srid)

