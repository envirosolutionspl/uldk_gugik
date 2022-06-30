import requests

URL = "http://uldk.gugik.gov.pl/"


def getRequest(id, request, result, srid):
    PARAMS = {'request': request, 'id': id, 'result': result, 'srid': srid}
    r = requests.get(url=URL, params=PARAMS)
    r_txt = r.text
    #print(r_txt)
    if r.status_code == 200 and not r_txt.startswith('-1'):
        if ";" in r_txt:
            return r_txt.split('\n')[1].split(';')[1]
        else:
            return r_txt.split('\n')[1]
    else:
        return None


def getParcelById(name, srid):
    request = "GetParcelByIdOrNr"
    result = "geom_wkt,teryt,parcel,region,commune,county,voivodeship"
    return getRequest(name, request, result, srid)

