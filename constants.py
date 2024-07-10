DEFAULT_SRID = 2180
ULDK_OBREB_DICT_URL = 'https://uldk.gugik.gov.pl/service.php?obiekt=obreb&wynik=nazwa,teryt'
ULDK_GMINA_DICT_URL = 'https://uldk.gugik.gov.pl/service.php?obiekt=gmina&wynik=gmina,teryt'
ULDK_POWIAT_DICT_URL = 'https://uldk.gugik.gov.pl/service.php?obiekt=powiat&wynik=powiat,teryt'
ULDK_WOJEWODZTWO_DICT_URL = 'https://uldk.gugik.gov.pl/service.php?obiekt=wojewodztwo&wynik=wojewodztwo,teryt'


DIALOG_MAPPING = {
    'rdb_bu': {
        'tab_title': 'Wybór obiektu prze identyfikator budynku',
        'sample_id': '141301_1.0010.713/2.5_BUD',
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
        'description_label': ' - dla obrębu: WWPPGG_R.OOOO"',
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
    'wojcomboBox': ('get_powiat_by_teryt', 'powcomboBox'),
    'powcomboBox': ('get_gmina_by_teryt', 'gmicomboBox'),
    'gmicomboBox': ('get_obreb_by_teryt', 'obrcomboBox'),
}

RADIOBUTTON_COMBOBOX_MAPPING = {
    'rdb_wo': 'wojcomboBox',
    'rdb_pw': 'powcomboBox',
    'rdb_gm': 'gmicomboBox',
    'rdb_ob': 'obrcomboBox',
}

COMBOBOX_RADIOBUTTON_MAPPING = {v: k for k, v in RADIOBUTTON_COMBOBOX_MAPPING.items()}

