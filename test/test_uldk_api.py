import base
import unittest
from unittest.mock import Mock, patch
from uldk_api import (
    getBuildingById, getParcelById, getRegionById,
    getCommuneById, getCountyById, getVoivodeshipById,
    DEFAULT_SRID,
    REQ_BUILDING_BY_ID, RES_BUILDING_BY_ID,
    REQ_PARCEL_BY_ID, RES_PARCEL_BY_ID,
    REQ_REGION_BY_ID, RES_REGION_BY_ID,
    REQ_COMMUNE_BY_ID, RES_COMMUNE_BY_ID,
    REQ_COUNTY_BY_ID, RES_COUNTY_BY_ID,
    REQ_VOIVODESHIP_BY_ID, RES_VOIVODESHIP_BY_ID,
)
from data.dane import ID_BUDYNKI, ID_DZIALKI, ID_OBREBY, ID_GMINY, ID_POWIATY, ID_WOJEWODZTWA


class TestUldkApi(unittest.TestCase):

    @patch('uldk_api.Request')
    def test_getBuildingById(self, mock_cls):
        for case in ID_BUDYNKI:
            with self.subTest(id=case["id"]):
                mock_cls.reset_mock()
                mock_cls.return_value = Mock(data=case["expected"])
                out = getBuildingById(case["id"], case["object_type"])
                self.assertEqual(out, case["expected"])
                mock_cls.assert_called_once_with(
                    {
                        "request": REQ_BUILDING_BY_ID,
                        "id": case["id"],
                        "result": ",".join(RES_BUILDING_BY_ID),
                        "srid": DEFAULT_SRID,
                    },
                    case["object_type"],
                )

    @patch('uldk_api.Request')
    def test_getParcelById(self, mock_cls):
        for case in ID_DZIALKI:
            with self.subTest(id=case["id"]):
                mock_cls.reset_mock()
                mock_cls.return_value = Mock(data=case["expected"])
                out = getParcelById(case["id"], case["object_type"])
                self.assertEqual(out, case["expected"])
                mock_cls.assert_called_once_with(
                    {
                        "request": REQ_PARCEL_BY_ID,
                        "id": case["id"],
                        "result": ",".join(RES_PARCEL_BY_ID),
                        "srid": DEFAULT_SRID,
                    },
                    case["object_type"],
                )

    @patch('uldk_api.Request')
    def test_getRegionById(self, mock_cls):
        for case in ID_OBREBY:
            with self.subTest(id=case["id"]):
                mock_cls.reset_mock()
                mock_cls.return_value = Mock(data=case["expected"])
                out = getRegionById(case["id"], case["object_type"])
                self.assertEqual(out, case["expected"])
                mock_cls.assert_called_once_with(
                    {
                        "request": REQ_REGION_BY_ID,
                        "id": case["id"],
                        "result": ",".join(RES_REGION_BY_ID),
                        "srid": DEFAULT_SRID,
                    },
                    case["object_type"],
                )

    @patch('uldk_api.Request')
    def test_getCommuneById(self, mock_cls):
        for case in ID_GMINY:
            with self.subTest(id=case["id"]):
                mock_cls.reset_mock()
                mock_cls.return_value = Mock(data=case["expected"])
                out = getCommuneById(case["id"], case["object_type"])
                self.assertEqual(out, case["expected"])
                mock_cls.assert_called_once_with(
                    {
                        "request": REQ_COMMUNE_BY_ID,
                        "id": case["id"],
                        "result": ",".join(RES_COMMUNE_BY_ID),
                        "srid": DEFAULT_SRID,
                    },
                    case["object_type"],
                )

    @patch('uldk_api.Request')
    def test_getCountyById(self, mock_cls):
        for case in ID_POWIATY:
            with self.subTest(id=case["id"]):
                mock_cls.reset_mock()
                mock_cls.return_value = Mock(data=case["expected"])
                out = getCountyById(case["id"], case["object_type"])
                self.assertEqual(out, case["expected"])
                mock_cls.assert_called_once_with(
                    {
                        "request": REQ_COUNTY_BY_ID,
                        "id": case["id"],
                        "result": ",".join(RES_COUNTY_BY_ID),
                        "srid": DEFAULT_SRID,
                    },
                    case["object_type"],
                )

    @patch('uldk_api.Request')
    def test_getVoivodeshipById(self, mock_cls):
        for case in ID_WOJEWODZTWA:
            with self.subTest(id=case["id"]):
                mock_cls.reset_mock()
                mock_cls.return_value = Mock(data=case["expected"])
                out = getVoivodeshipById(case["id"], case["object_type"])
                self.assertEqual(out, case["expected"])
                mock_cls.assert_called_once_with(
                    {
                        "request": REQ_VOIVODESHIP_BY_ID,
                        "id": case["id"],
                        "result": ",".join(RES_VOIVODESHIP_BY_ID),
                        "srid": DEFAULT_SRID,
                    },
                    case["object_type"],
                )
