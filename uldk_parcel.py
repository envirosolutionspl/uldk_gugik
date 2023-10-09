from .request import Request


def getParcelById(name, srid, **kwargs):
    request = "GetParcelByIdOrNr"
    result = "geom_wkt,teryt,parcel,region,commune,county,voivodeship"
    params = {'request': request, 'id': name, 'result': result, 'srid': srid}
    res = Request(params, **kwargs)
    return res.data



# def getArkusz(id, request, result):
#     PARAMS = {'request': request, 'id': id, 'result': result}
#     rq = Request(params=PARAMS, **kwargs)
#     print('link_arkusz: ', rq.text)
#     print('status', rq.status_code)
#     rq_txt = rq.text
#     if rq.status_code == 200 and not rq_txt.startswith('-1'):
#         return rq_txt.split('\n')
#     elif rq.status_code == 200 and rq_txt.find("usługa nie zwróciła odpowiedzi"):
#         rq2 = Request(params=PARAMS, **kwargs)
#         rq2_txt = rq2.text
#         print("Arkusz: ",rq2_txt)
#         if rq2.status_code == 200 and not rq2_txt.startswith('-1'):
#             return rq2_txt.split('\n')
#             print("Arkusz2222: ", rq2_txt.split('\n'))
#         else:
#             return None
#     else:
#         return None
#
#
# def getParcelById2(name):
#     request = "GetParcelById"
#     result = "teryt"
#     return getArkusz(name, request, result)
