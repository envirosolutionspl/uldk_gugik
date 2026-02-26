WKT_POLYGON = "POLYGON((0 0,1 0,1 1,0 1,0 0))"

MIASTA = [
    {"xy": "500629,639049",
     "teryt_budynku": "146501_1.0001.123_BUD",
     "teryt_dzialki": "146501_1.0001.123/4", "numer_dzialki": "123/4",
     "teryt_obrebu": "146501_1.0001", "numer_obrebu": "0001",
     "teryt_gminy": "146501_1", "nazwa_gminy": "Warszawa",
     "teryt_powiatu": "1465", "nazwa_powiatu": "m. st. Warszawa",
     "teryt_wojewodztwa": "14", "nazwa_wojewodztwa": "mazowieckie"},
    {"xy": "424049,237499",
     "teryt_budynku": "126101_1.0001.456_BUD",
     "teryt_dzialki": "126101_1.0001.456/7", "numer_dzialki": "456/7",
     "teryt_obrebu": "126101_1.0001", "numer_obrebu": "0001",
     "teryt_gminy": "126101_1", "nazwa_gminy": "Kraków",
     "teryt_powiatu": "1261", "nazwa_powiatu": "Kraków",
     "teryt_wojewodztwa": "12", "nazwa_wojewodztwa": "małopolskie"},
    {"xy": "501849,721789",
     "teryt_budynku": "226101_1.0004.89_BUD",
     "teryt_dzialki": "226101_1.0004.89/1", "numer_dzialki": "89/1",
     "teryt_obrebu": "226101_1.0004", "numer_obrebu": "0004",
     "teryt_gminy": "226101_1", "nazwa_gminy": "Gdańsk",
     "teryt_powiatu": "2261", "nazwa_powiatu": "Gdańsk",
     "teryt_wojewodztwa": "22", "nazwa_wojewodztwa": "pomorskie"},
    {"xy": "363589,504129",
     "teryt_budynku": "306401_1.0002.12_BUD",
     "teryt_dzialki": "306401_1.0002.12", "numer_dzialki": "12",
     "teryt_obrebu": "306401_1.0002", "numer_obrebu": "0002",
     "teryt_gminy": "306401_1", "nazwa_gminy": "Poznań",
     "teryt_powiatu": "3064", "nazwa_powiatu": "Poznań",
     "teryt_wojewodztwa": "30", "nazwa_wojewodztwa": "wielkopolskie"},
    {"xy": "365489,363209",
     "teryt_budynku": "026401_1.0003.77_BUD",
     "teryt_dzialki": "026401_1.0003.77/2", "numer_dzialki": "77/2",
     "teryt_obrebu": "026401_1.0003", "numer_obrebu": "0003",
     "teryt_gminy": "026401_1", "nazwa_gminy": "Wrocław",
     "teryt_powiatu": "0264", "nazwa_powiatu": "Wrocław",
     "teryt_wojewodztwa": "02", "nazwa_wojewodztwa": "dolnośląskie"},
]

XY_BUDYNKI     = [{"xy": m["xy"], "object_type": 6, "expected": f"{WKT_POLYGON}|{m['teryt_budynku']}|{m['numer_obrebu']}|{m['nazwa_gminy']}|{m['nazwa_powiatu']}|{m['nazwa_wojewodztwa']}"} for m in MIASTA]
XY_DZIALKI     = [{"xy": m["xy"], "object_type": 1, "expected": f"{WKT_POLYGON}|{m['teryt_dzialki']}|{m['numer_dzialki']}|{m['numer_obrebu']}|{m['nazwa_gminy']}|{m['nazwa_powiatu']}|{m['nazwa_wojewodztwa']}"} for m in MIASTA]
XY_OBREBY      = [{"xy": m["xy"], "object_type": 2, "expected": f"{WKT_POLYGON}|{m['teryt_obrebu']}|{m['numer_obrebu']}|{m['nazwa_gminy']}|{m['nazwa_powiatu']}|{m['nazwa_wojewodztwa']}"} for m in MIASTA]
XY_GMINY       = [{"xy": m["xy"], "object_type": 3, "expected": f"{WKT_POLYGON}|{m['teryt_gminy']}|{m['nazwa_gminy']}|{m['nazwa_powiatu']}|{m['nazwa_wojewodztwa']}"} for m in MIASTA]
XY_POWIATY     = [{"xy": m["xy"], "object_type": 4, "expected": f"{WKT_POLYGON}|{m['teryt_powiatu']}|{m['nazwa_powiatu']}|{m['nazwa_wojewodztwa']}"} for m in MIASTA]
XY_WOJEWODZTWA = [{"xy": m["xy"], "object_type": 5, "expected": f"{WKT_POLYGON}|{m['teryt_wojewodztwa']}|{m['nazwa_wojewodztwa']}"} for m in MIASTA]

ID_BUDYNKI     = [{"id": m["teryt_budynku"], "object_type": 6, "expected": f"{WKT_POLYGON}|{m['teryt_budynku']}|{m['numer_obrebu']}|{m['nazwa_gminy']}|{m['nazwa_powiatu']}|{m['nazwa_wojewodztwa']}"} for m in MIASTA]
ID_DZIALKI     = [{"id": m["teryt_dzialki"],  "object_type": 1, "expected": f"{WKT_POLYGON}|{m['teryt_dzialki']}|{m['numer_dzialki']}|{m['numer_obrebu']}|{m['nazwa_gminy']}|{m['nazwa_powiatu']}|{m['nazwa_wojewodztwa']}"} for m in MIASTA]
ID_OBREBY      = [{"id": m["teryt_obrebu"], "object_type": 2, "expected": f"{WKT_POLYGON}|{m['teryt_obrebu']}|{m['numer_obrebu']}|{m['nazwa_gminy']}|{m['nazwa_powiatu']}|{m['nazwa_wojewodztwa']}"} for m in MIASTA]
ID_GMINY       = [{"id": m["teryt_gminy"],  "object_type": 3, "expected": f"{WKT_POLYGON}|{m['teryt_gminy']}|{m['nazwa_gminy']}|{m['nazwa_powiatu']}|{m['nazwa_wojewodztwa']}"} for m in MIASTA]
ID_POWIATY     = [{"id": m["teryt_powiatu"], "object_type": 4, "expected": f"{WKT_POLYGON}|{m['teryt_powiatu']}|{m['nazwa_powiatu']}|{m['nazwa_wojewodztwa']}"} for m in MIASTA]
ID_WOJEWODZTWA = [{"id": m["teryt_wojewodztwa"], "object_type": 5, "expected": f"{WKT_POLYGON}|{m['teryt_wojewodztwa']}|{m['nazwa_wojewodztwa']}"} for m in MIASTA]

PARCEL_BY_ID_SEARCH = [{"name": m["teryt_dzialki"], "object_type": 1, "expected": f"{WKT_POLYGON}|{m['teryt_dzialki']}|{m['numer_dzialki']}|{m['numer_obrebu']}|{m['nazwa_gminy']}|{m['nazwa_powiatu']}|{m['nazwa_wojewodztwa']}"} for m in MIASTA]
PARCEL_BY_ID        = [{"name": m["teryt_dzialki"], "expected": {f"{WKT_POLYGON}|{m['teryt_dzialki']}|{m['numer_dzialki']}|{m['numer_obrebu']}|{m['nazwa_gminy']}|{m['nazwa_powiatu']}|{m['nazwa_wojewodztwa']}"}} for m in MIASTA]
REGION_BY_ID        = [{"id": m["teryt_obrebu"], "expected": {f"{WKT_POLYGON}|{m['teryt_obrebu']}|{m['numer_obrebu']}|{m['nazwa_gminy']}|{m['nazwa_powiatu']}|{m['nazwa_wojewodztwa']}"}} for m in MIASTA]
