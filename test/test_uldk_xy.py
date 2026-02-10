import base
import unittest
from unittest.mock import Mock, patch
from uldk_xy import (
    getBuildingByXY, getParcelByXY, getRegionByXY,
    getCommuneByXY, getCountyByXY, getVoivodeshipByXY,
    DEFAULT_SRID,
    REQ_BUILDING_BY_XY, RES_BUILDING_BY_XY,
    REQ_PARCEL_BY_XY, RES_PARCEL_BY_XY,
    REQ_REGION_BY_XY, RES_REGION_BY_XY,
    REQ_COMMUNE_BY_XY, RES_COMMUNE_BY_XY,
    REQ_COUNTY_BY_XY, RES_COUNTY_BY_XY,
    REQ_VOIVODESHIP_BY_XY, RES_VOIVODESHIP_BY_XY,
)
from data.dane import XY_BUDYNKI, XY_DZIALKI, XY_OBREBY, XY_GMINY, XY_POWIATY, XY_WOJEWODZTWA


class TestUldkXY(unittest.TestCase):

    @patch('uldk_xy.Request')
    def test_getBuildingByXY(self, mock_cls):
        for case in XY_BUDYNKI:
            with self.subTest(xy=case["xy"]):
                mock_cls.reset_mock()
                mock_cls.return_value = Mock(data=case["expected"])
                out = getBuildingByXY(case["xy"], case["object_type"])
                self.assertEqual(out, case["expected"])
                mock_cls.assert_called_once_with(
                    {"request": REQ_BUILDING_BY_XY, "xy": case["xy"],
                     "result": ",".join(RES_BUILDING_BY_XY), "srid": DEFAULT_SRID},
                    case["object_type"])

    @patch('uldk_xy.Request')
    def test_getParcelByXY(self, mock_cls):
        for case in XY_DZIALKI:
            with self.subTest(xy=case["xy"]):
                mock_cls.reset_mock()
                mock_cls.return_value = Mock(data=case["expected"])
                out = getParcelByXY(case["xy"], case["object_type"])
                self.assertEqual(out, case["expected"])
                mock_cls.assert_called_once_with(
                    {"request": REQ_PARCEL_BY_XY, "xy": case["xy"],
                     "result": ",".join(RES_PARCEL_BY_XY), "srid": DEFAULT_SRID},
                    case["object_type"])

    @patch('uldk_xy.Request')
    def test_getRegionByXY(self, mock_cls):
        for case in XY_OBREBY:
            with self.subTest(xy=case["xy"]):
                mock_cls.reset_mock()
                mock_cls.return_value = Mock(data=case["expected"])
                out = getRegionByXY(case["xy"], case["object_type"])
                self.assertEqual(out, case["expected"])
                mock_cls.assert_called_once_with(
                    {"request": REQ_REGION_BY_XY, "xy": case["xy"],
                     "result": ",".join(RES_REGION_BY_XY), "srid": DEFAULT_SRID},
                    case["object_type"])

    @patch('uldk_xy.Request')
    def test_getCommuneByXY(self, mock_cls):
        for case in XY_GMINY:
            with self.subTest(xy=case["xy"]):
                mock_cls.reset_mock()
                mock_cls.return_value = Mock(data=case["expected"])
                out = getCommuneByXY(case["xy"], case["object_type"])
                self.assertEqual(out, case["expected"])
                mock_cls.assert_called_once_with(
                    {"request": REQ_COMMUNE_BY_XY, "xy": case["xy"],
                     "result": ",".join(RES_COMMUNE_BY_XY), "srid": DEFAULT_SRID},
                    case["object_type"])

    @patch('uldk_xy.Request')
    def test_getCountyByXY(self, mock_cls):
        for case in XY_POWIATY:
            with self.subTest(xy=case["xy"]):
                mock_cls.reset_mock()
                mock_cls.return_value = Mock(data=case["expected"])
                out = getCountyByXY(case["xy"], case["object_type"])
                self.assertEqual(out, case["expected"])
                mock_cls.assert_called_once_with(
                    {"request": REQ_COUNTY_BY_XY, "xy": case["xy"],
                     "result": ",".join(RES_COUNTY_BY_XY), "srid": DEFAULT_SRID},
                    case["object_type"])

    @patch('uldk_xy.Request')
    def test_getVoivodeshipByXY(self, mock_cls):
        for case in XY_WOJEWODZTWA:
            with self.subTest(xy=case["xy"]):
                mock_cls.reset_mock()
                mock_cls.return_value = Mock(data=case["expected"])
                out = getVoivodeshipByXY(case["xy"], case["object_type"])
                self.assertEqual(out, case["expected"])
                mock_cls.assert_called_once_with(
                    {"request": REQ_VOIVODESHIP_BY_XY, "xy": case["xy"],
                     "result": ",".join(RES_VOIVODESHIP_BY_XY), "srid": DEFAULT_SRID},
                    case["object_type"])
