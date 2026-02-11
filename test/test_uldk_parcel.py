import base
import unittest
from unittest.mock import Mock, patch
from uldk_parcel import (
    getParcelByIdSearch, getParcelById, getRegionById,
    DEFAULT_SRID, PARCEL_BY_ID_OR_NR, REQ_REGION_BY_ID, RES_REGION_META,
)
from data.dane import PARCEL_BY_ID_SEARCH, PARCEL_BY_ID, REGION_BY_ID


class TestUldkParcel(unittest.TestCase):

    @patch('uldk_parcel.RQ')
    def test_getParcelByIdSearch(self, mock_cls):
        for case in PARCEL_BY_ID_SEARCH:
            with self.subTest(name=case["name"]):
                mock_cls.reset_mock()
                mock_cls.return_value = Mock(data=case["expected"])
                out = getParcelByIdSearch(case["name"], case["object_type"])
                self.assertEqual(out, case["expected"])
                mock_cls.assert_called_once_with(
                    {
                        "request": PARCEL_BY_ID_OR_NR["request"],
                        "id": case["name"],
                        "result": ",".join(PARCEL_BY_ID_OR_NR["result"]),
                        "srid": DEFAULT_SRID,
                    },
                    case["object_type"],
                )

    @patch('uldk_parcel.RS')
    def test_getParcelById(self, mock_cls):
        for case in PARCEL_BY_ID:
            with self.subTest(name=case["name"]):
                mock_cls.reset_mock()
                mock_cls.return_value = Mock(data=case["expected"])
                out = getParcelById(case["name"])
                self.assertEqual(out, case["expected"])
                mock_cls.assert_called_once_with(
                    {
                        "request": PARCEL_BY_ID_OR_NR["request"],
                        "id": case["name"],
                        "result": ",".join(PARCEL_BY_ID_OR_NR["result"]),
                        "srid": DEFAULT_SRID,
                    },
                )

    @patch('uldk_parcel.RR')
    def test_getRegionById(self, mock_cls):
        for case in REGION_BY_ID:
            with self.subTest(id=case["id"]):
                mock_cls.reset_mock()
                mock_cls.return_value = Mock(data=case["expected"])
                out = getRegionById(case["id"])
                self.assertEqual(out, case["expected"])
                mock_cls.assert_called_once_with(
                    {
                        "request": REQ_REGION_BY_ID,
                        "id": case["id"],
                        "result": ",".join(RES_REGION_META),
                        "srid": DEFAULT_SRID,
                    },
                )
