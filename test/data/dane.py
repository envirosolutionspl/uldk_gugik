W = "POLYGON((0 0,1 0,1 1,0 1,0 0))"

MIASTA = [
    {"xy": "500629,639049", "bud": "146501_1.0001.123_BUD", "dz": "146501_1.0001.123/4", "nr": "123/4",
     "obr": "146501_1.0001", "ob": "0001", "gm": "146501_1", "g": "Warszawa",
     "pow": "1465", "p": "m. st. Warszawa", "woj": "14", "w": "mazowieckie"},
    {"xy": "424049,237499", "bud": "126101_1.0001.456_BUD", "dz": "126101_1.0001.456/7", "nr": "456/7",
     "obr": "126101_1.0001", "ob": "0001", "gm": "126101_1", "g": "Kraków",
     "pow": "1261", "p": "Kraków", "woj": "12", "w": "małopolskie"},
    {"xy": "501849,721789", "bud": "226101_1.0004.89_BUD", "dz": "226101_1.0004.89/1", "nr": "89/1",
     "obr": "226101_1.0004", "ob": "0004", "gm": "226101_1", "g": "Gdańsk",
     "pow": "2261", "p": "Gdańsk", "woj": "22", "w": "pomorskie"},
    {"xy": "363589,504129", "bud": "306401_1.0002.12_BUD", "dz": "306401_1.0002.12", "nr": "12",
     "obr": "306401_1.0002", "ob": "0002", "gm": "306401_1", "g": "Poznań",
     "pow": "3064", "p": "Poznań", "woj": "30", "w": "wielkopolskie"},
    {"xy": "365489,363209", "bud": "026401_1.0003.77_BUD", "dz": "026401_1.0003.77/2", "nr": "77/2",
     "obr": "026401_1.0003", "ob": "0003", "gm": "026401_1", "g": "Wrocław",
     "pow": "0264", "p": "Wrocław", "woj": "02", "w": "dolnośląskie"},
]

XY_BUDYNKI     = [{"xy": m["xy"], "object_type": 6, "expected": f"{W}|{m['bud']}|{m['ob']}|{m['g']}|{m['p']}|{m['w']}"} for m in MIASTA]
XY_DZIALKI     = [{"xy": m["xy"], "object_type": 1, "expected": f"{W}|{m['dz']}|{m['nr']}|{m['ob']}|{m['g']}|{m['p']}|{m['w']}"} for m in MIASTA]
XY_OBREBY      = [{"xy": m["xy"], "object_type": 2, "expected": f"{W}|{m['obr']}|{m['ob']}|{m['g']}|{m['p']}|{m['w']}"} for m in MIASTA]
XY_GMINY       = [{"xy": m["xy"], "object_type": 3, "expected": f"{W}|{m['gm']}|{m['g']}|{m['p']}|{m['w']}"} for m in MIASTA]
XY_POWIATY     = [{"xy": m["xy"], "object_type": 4, "expected": f"{W}|{m['pow']}|{m['p']}|{m['w']}"} for m in MIASTA]
XY_WOJEWODZTWA = [{"xy": m["xy"], "object_type": 5, "expected": f"{W}|{m['woj']}|{m['w']}"} for m in MIASTA]

ID_BUDYNKI     = [{"id": m["bud"], "object_type": 6, "expected": f"{W}|{m['bud']}|{m['ob']}|{m['g']}|{m['p']}|{m['w']}"} for m in MIASTA]
ID_DZIALKI     = [{"id": m["dz"],  "object_type": 1, "expected": f"{W}|{m['dz']}|{m['nr']}|{m['ob']}|{m['g']}|{m['p']}|{m['w']}"} for m in MIASTA]
ID_OBREBY      = [{"id": m["obr"], "object_type": 2, "expected": f"{W}|{m['obr']}|{m['ob']}|{m['g']}|{m['p']}|{m['w']}"} for m in MIASTA]
ID_GMINY       = [{"id": m["gm"],  "object_type": 3, "expected": f"{W}|{m['gm']}|{m['g']}|{m['p']}|{m['w']}"} for m in MIASTA]
ID_POWIATY     = [{"id": m["pow"], "object_type": 4, "expected": f"{W}|{m['pow']}|{m['p']}|{m['w']}"} for m in MIASTA]
ID_WOJEWODZTWA = [{"id": m["woj"], "object_type": 5, "expected": f"{W}|{m['woj']}|{m['w']}"} for m in MIASTA]

PARCEL_BY_ID  = [{"name": m["dz"], "object_type": 1, "expected": f"{W}|{m['dz']}|{m['nr']}|{m['ob']}|{m['g']}|{m['p']}|{m['w']}"} for m in MIASTA]
PARCEL_BY_ID2 = [{"name": m["dz"], "expected": {f"{W}|{m['dz']}|{m['nr']}|{m['ob']}|{m['g']}|{m['p']}|{m['w']}"}} for m in MIASTA]
REGION_BY_ID  = [{"id": m["obr"], "expected": {f"{W}|{m['obr']}|{m['ob']}|{m['g']}|{m['p']}|{m['w']}"}} for m in MIASTA]
