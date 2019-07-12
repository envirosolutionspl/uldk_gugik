import requests
from qgis.core import QgsVectorLayer, QgsGeometry, QgsFeature, QgsProject

URL = "http://uldk.gugik.gov.pl/"


def getRequestTeryt(xy, request):
    PARAMS = {'request': request, 'xy': xy, 'result': 'teryt'}
    r = requests.get(url=URL, params=PARAMS)
    r_txt = r.text

    #print(r_txt)
    if r.status_code == 200 and r_txt[0] == '0':
        return r_txt.split('\n')[1]
    else:
        print(r_txt)
        return None