DEFAULT_SRID = 2180
ULDK_OBREB_DICT_URL = 'https://uldk.gugik.gov.pl/service.php?obiekt=obreb&wynik=nazwa,teryt&teryt='
ULDK_GMINA_DICT_URL = 'https://uldk.gugik.gov.pl/service.php?obiekt=gmina&wynik=gmina,teryt&teryt='
ULDK_POWIAT_DICT_URL = 'https://uldk.gugik.gov.pl/service.php?obiekt=powiat&wynik=powiat,teryt&teryt='
ULDK_WOJEWODZTWO_DICT_URL = 'https://uldk.gugik.gov.pl/service.php?obiekt=wojewodztwo&wynik=wojewodztwo,teryt'

# REST API endpoints (nowe API)
REST_API_BASE_URL = "https://rest.envirosolutions.pl/dzialki"
REST_ENDPOINT_VOIVODESHIP = "/getVoivodeship"
REST_ENDPOINT_COUNTY = "/getCounty"
REST_ENDPOINT_COMMUNE = "/getCommune"
REST_ENDPOINT_PRECINCT = "/getPrecinct"
LOG_TAG = "TerytFetch"

FEED_URL = 'https://qgisfeed.envirosolutions.pl/'

INDUSTRIES = {
    "999": "Nie wybrano",
    "e": "Energetyka/OZE",
    "u": "Urząd",
    "td": "Transport/Drogi",
    "pg": "Planowanie/Geodezja",
    "wk": "WodKan",
    "s": "Środowisko",
    "rl": "Rolnictwo/Leśnictwo",
    "tk": "Telkom",
    "edu": "Edukacja",
    "i": "Inne",
    "it": "IT",
    "n": "Nieruchomości"
}

ULDK_BASE_URL = "https://uldk.gugik.gov.pl/"
ULDK_NO_RESULTS = "-1 brak wyników"
ULDK_XML_MARKER = "XML"
ULDK_ERROR_MARKERS = ["błęd"]
ENCODING_SYSTEM = "utf-8"
ULDK_MIN_LINE_LEN = 3  # Do filtrowania zbyt krótkich odpowiedzi z serwera
ULDK_NOT_FOUND = -1  # Wartość zwracana przez metodę find() gdy nie znajdzie tekstu
ULDK_OBJ_REGION = 2  # Typ obiektu dla obrębu ewidencyjnego (region) z API ULDK
ULDK_TERYT_SUFFIX_LEN = 4  # Kilka działek ma ten sam TERYT, mimo że należy do tego samego terenu -> ignorujemy 4 ostatnie cyfry


DIALOG_MAPPING = {
    'rdb_bu': {
        'tab_title': 'Wybór obiektu przez identyfikator budynku',
        'sample_id': '142608_2.0022.108_BUD',
        'description_label': ' - dla budynków: WWPPGG_R.OOOO.NR_DZ.Nr_BUD, WWPPGG_R.OOOO.AR_NR.NR_DZ.Nr_BUD lub WWPPGG_R.OOOO.Nr_BUD',
    },
    'rdb_dz': {
        'tab_title': 'Wybór obiektu przez nazwę obrębu i numer działki',
        'sample_id': '141301_1.0010.713/2',
        'description_label': ' - dla działki: WWPPGG_R.OOOO.[AR_NR].NR_DZ, WWPPGG_R.OOOO.NR_DZ',
    },
    'rdb_ob': {
        'tab_title': 'Wybór obiektu przez nazwę obrębu',
        'sample_id': '141301_1.0010',
        'description_label': ' - dla obrębu: WWPPGG_R.OOOO',
    },
    'rdb_gm': {
        'tab_title': 'Wybór obiektu przez nazwę gminy',
        'sample_id': '141301_1',
        'description_label': ' - dla gminy: WWPPGG_R',
    },
    'rdb_pw': {
        'tab_title': 'Wybór obiektu przez nazwę powiatu',
        'sample_id': '1413',
        'description_label': ' - dla powiatu: WWPP',
    },
    'rdb_wo': {
        'tab_title': 'Wybór obiektu przez nazwę województwa',
        'sample_id': '14',
        'description_label': ' - dla województwa: WW',
    },
}
ADMINISTRATIVE_UNITS_OBJECTS = {
    'wojcomboBox': ('getPowiatByTeryt', 'powcomboBox'),
    'powcomboBox': ('getGminaByTeryt', 'gmicomboBox'),
    'gmicomboBox': ('getObrebByTeryt', 'obrcomboBox'),
}
RADIOBUTTON_COMBOBOX_MAPPING = {
    'rdb_wo': 'wojcomboBox',
    'rdb_pw': 'powcomboBox',
    'rdb_gm': 'gmicomboBox',
    'rdb_ob': 'obrcomboBox',
    'rdb_dz': 'arkcomboBox',
}

COMBOBOX_RADIOBUTTON_MAPPING = {v: k for k, v in RADIOBUTTON_COMBOBOX_MAPPING.items()}

REQ_BUILDING_BY_ID = "GetBuildingById"
REQ_PARCEL_BY_ID = "GetParcelById"
REQ_REGION_BY_ID = "GetRegionById"
REQ_COMMUNE_BY_ID = "GetCommuneById"
REQ_COUNTY_BY_ID = "GetCountyById"
REQ_VOIVODESHIP_BY_ID = "GetVoivodeshipById"

RES_BUILDING_BY_ID = ["geom_wkt", "teryt", "region", "commune", "county", "voivodeship"]
RES_PARCEL_BY_ID = ["geom_wkt", "teryt", "parcel", "region", "commune", "county", "voivodeship"]
RES_REGION_BY_ID = ["geom_wkt", "teryt", "region", "commune", "county", "voivodeship"]
RES_COMMUNE_BY_ID = ["geom_wkt", "teryt", "commune", "county", "voivodeship"]
RES_COUNTY_BY_ID = ["geom_wkt", "teryt", "county", "voivodeship"]
RES_VOIVODESHIP_BY_ID = ["geom_wkt", "teryt", "voivodeship"]

COMBOBOX_STYLES = {
    "visible": "QComboBox { color: black }",
    "hidden": "QComboBox { color: transparent }"
}

PARCEL_BY_ID_OR_NR = {
    "request": "GetParcelByIdOrNr",
    "result": ["geom_wkt", "teryt", "parcel", "region", "commune", "county", "voivodeship"]
}

RES_REGION_META = ["teryt", "region", "commune", "county", "voivodeship"]

ULDK_RESULT_TERYT = "teryt"

REQ_BUILDING_BY_XY = "GetBuildingByXY"
REQ_PARCEL_BY_XY = "GetParcelByXY"
REQ_REGION_BY_XY = "GetRegionByXY"
REQ_COMMUNE_BY_XY = "GetCommuneByXY"
REQ_COUNTY_BY_XY = "GetCountyByXY"
REQ_VOIVODESHIP_BY_XY = "GetVoivodeshipByXY"

RES_BUILDING_BY_XY = ["geom_wkt", "teryt", "region", "commune", "county", "voivodeship"]
RES_PARCEL_BY_XY = ["geom_wkt", "teryt", "parcel", "region", "commune", "county", "voivodeship"]
RES_REGION_BY_XY = ["geom_wkt", "teryt", "region", "commune", "county", "voivodeship"]
RES_COMMUNE_BY_XY = ["geom_wkt", "teryt", "commune", "county", "voivodeship"]
RES_COUNTY_BY_XY = ["geom_wkt", "teryt", "county", "voivodeship"]
RES_VOIVODESHIP_BY_XY = ["geom_wkt", "teryt", "voivodeship"]

CHECK_INTERNET_CLIENT = {
    "host": "www.google.com",
    "port": 80,
    "timeout": 2
}

ENV_MENU_NAME = "EnviroSolutions"

SWAP_XY_SRIDS = {"2180", "4326", "3857", "2176", "2177", "2178", "2179"}

TOOLTIP_FROM_MAP = "skrót: ALT + F"

OBJECT_TYPES = {
    1: {
        "layer_name": "dzialki_ew_uldk",
        "success_label": "działkę o nr teryt: %s"
    },
    2: {
        "layer_name": "obreby_ew_uldk",
        "success_label": "obręb ewidencyjny"
    },
    3: {
        "layer_name": "gminy_uldk",
        "success_label": "gminę"
    },
    4: {
        "layer_name": "powiaty_uldk",
        "success_label": "powiat"
    },
    5: {
        "layer_name": "wojewodztwa_uldk",
        "success_label": "województwo"
    },
    6: {
        "layer_name": "budynki_uldk",
        "success_label": "budynek"
    }
}
