DEFAULT_SRID = 2180
ULDK_OBREB_DICT_URL = 'https://uldk.gugik.gov.pl/service.php?obiekt=obreb&wynik=nazwa,teryt&teryt='
ULDK_GMINA_DICT_URL = 'https://uldk.gugik.gov.pl/service.php?obiekt=gmina&wynik=gmina,teryt&teryt='
ULDK_POWIAT_DICT_URL = 'https://uldk.gugik.gov.pl/service.php?obiekt=powiat&wynik=powiat,teryt&teryt='
ULDK_WOJEWODZTWO_DICT_URL = 'https://uldk.gugik.gov.pl/service.php?obiekt=wojewodztwo&wynik=wojewodztwo,teryt'
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

ULDK_BASE_URL = "http://uldk.gugik.gov.pl/"
ULDK_NO_RESULTS = "-1 brak wyników"
ULDK_XML_MARKER = "XML"
ULDK_ERROR_MARKER = "błęd"
ULDK_ENCODING = "utf-8"
ULDK_MIN_LINE_LEN = 3
ULDK_NOT_FOUND = -1
ULDK_OBJ_REGION = 2
ULDK_TERYT_SUFFIX_LEN = 4


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

RES_BUILDING_BY_ID = "geom_wkt,teryt,region,commune,county,voivodeship"
RES_PARCEL_BY_ID = "geom_wkt,teryt,parcel,region,commune,county,voivodeship"
RES_REGION_BY_ID = "geom_wkt,teryt,region,commune,county,voivodeship"
RES_COMMUNE_BY_ID = "geom_wkt,teryt,commune,county,voivodeship"
RES_COUNTY_BY_ID = "geom_wkt,teryt,county,voivodeship"
RES_VOIVODESHIP_BY_ID = "geom_wkt,teryt,voivodeship"

ULDK_NO_INTERNET = "Brak połączenia z Internetem. Spróbuj ponownie później"
ULDK_LOG = "ULDK"
COMBOBOX_STYLE_VISIBLE = "QComboBox { color: black }"
COMBOBOX_STYLE_HIDDEN = "QComboBox { color: transparent }"

REQ_PARCEL_BY_ID_OR_NR = "GetParcelByIdOrNr"
RES_PARCEL_BY_ID_OR_NR = "geom_wkt,teryt,parcel,region,commune,county,voivodeship"

REQ_REGION_BY_ID = "GetRegionById"
RES_REGION_META = "teryt,region,commune,county,voivodeship"

ULDK_RESULT_TERYT = "teryt"

REQ_BUILDING_BY_XY = "GetBuildingByXY"
REQ_PARCEL_BY_XY = "GetParcelByXY"
REQ_REGION_BY_XY = "GetRegionByXY"
REQ_COMMUNE_BY_XY = "GetCommuneByXY"
REQ_COUNTY_BY_XY = "GetCountyByXY"
REQ_VOIVODESHIP_BY_XY = "GetVoivodeshipByXY"

RES_BUILDING_BY_XY = "geom_wkt,teryt,region,commune,county,voivodeship"
RES_PARCEL_BY_XY = "geom_wkt,teryt,parcel,region,commune,county,voivodeship"
RES_REGION_BY_XY = "geom_wkt,teryt,region,commune,county,voivodeship"
RES_COMMUNE_BY_XY = "geom_wkt,teryt,commune,county,voivodeship"
RES_COUNTY_BY_XY = "geom_wkt,teryt,county,voivodeship"
RES_VOIVODESHIP_BY_XY = "geom_wkt,teryt,voivodeship"

INTERNET_HOST = "www.google.com"
INTERNET_PORT = 80
INTERNET_TIMEOUT = 2
MSG_CONNECTION_ERROR = "Błąd połączenia: {error}"

ENV_MENU_NAME = "&EnviroSolutions"
ENV_TOOLBAR_NAME = "EnviroSolutions"

SWAP_XY_SRIDS = {"2180", "4326", "3857", "2176", "2177", "2178", "2179"}

LAYER_NAMES_BY_TYPE = {
    1: "dzialki_ew_uldk",
    2: "obreby_ew_uldk",
    3: "gminy_uldk",
    4: "powiaty_uldk",
    5: "wojewodztwa_uldk",
    6: "budynki_uldk",
}

ICON_ULDK_PATH = ':/plugins/uldk_gugik/images/uldk.svg'
ICON_COORDS_PATH = ':/plugins/uldk_gugik/images/coords.png'
TOOLTIP_FROM_MAP = "skrót: ALT + F"

MSG_PREFIX_WARNING = "Ostrzeżenie:"
MSG_PREFIX_FORM_ERROR = "Błąd formularza:"
MSG_PREFIX_FETCH_ERROR = "Nie udało się pobrać obiektu:"
MSG_PREFIX_INFO = "Informacja:"
MSG_PREFIX_SUCCESS = "Sukces:"

MSG_NO_CRS_TITLE = "Projekt QGIS nie posiada zdefiniowanego układu współrzędnych."
MSG_NO_CRS_BODY = "W celu dalszej pracy zdefiniuj układ współrzędnych dla projektu"
MSG_ULDK_SERVER_DOWN = "Serwer ULDK nie odpowiada. Spróbuj ponownie później"
ULDK_NO_INTERNET_SHORT = "Brak połączenia z internetem"

MSG_MISSING_ID = "musisz wpisać identyfikator"
MSG_MISSING_REGION = "musisz wpisać obręb"
MSG_MISSING_PARCEL = "musisz wpisać numer działki"
MSG_MISSING_X = "musisz wpisać współrzędną X"
MSG_MISSING_Y = "musisz wpisać współrzędną Y"

MSG_NO_PARCEL_RESULTS = "Nie zwrócono żadnej działki dla podanych parametrów"
MSG_NO_PARCEL_DOWNLOADED = "Nie pobrano żadnej działki dla podanych parametrów"

INFO_PARCELS_FOUND = "Znaleziono działkę/i dla podanych parametrów, wybierz numer arkusza."
INFO_PARCEL_FOUND = "Znaleziono działkę dla podanych parametrów. Aby pobrać działkę, kliknij przycisk Pobierz."

MSG_API_NO_RESPONSE = "API nie zwróciło odpowiedzi dla żądanego zapytania"
MSG_API_NO_OBJECT_ID = "API nie zwróciło obiektu dla id {id}"
MSG_API_NO_GEOM_ID = "API nie zwróciło geometrii dla id {id}"
MSG_API_NO_OBJECT_QUERY = "API nie zwróciło obiektu dla wybranego zapytania"
MSG_API_NO_OBJECT_COORDS = "API nie zwróciło obiektu dla współrzędnych {coords}"
MSG_MORE_PARCELS_HINT = (
    "W wybranym obrębie znaleziono więcej działek o identyfikatorze TERYT: {teryt}. "
    "Dodaj numer arkusza w celu odnalezienia właściwej działki"
)
MSG_PARCEL_SUCCESS = "Pobrano działkę dla obiektu: {name}"

OBJECT_TYPE_SUCCESS_LABELS = {
    1: "działkę o nr teryt: %s",
    2: "obręb ewidencyjny",
    3: "gminę",
    4: "powiat",
    5: "województwo",
    6: "budynek",
}