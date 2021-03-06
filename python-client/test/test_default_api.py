"""
    Deutscher Wetterdienst: API

    Aktuelle Wetterdaten von allen Deutschen Wetterstationen  # noqa: E501

    The version of the OpenAPI document: 1.2.0
    Contact: kontakt@bund.dev
    Generated by: https://openapi-generator.tech
"""


import unittest

from deutschland.dwd.api.default_api import DefaultApi  # noqa: E501

from deutschland import dwd


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_alpen_forecast_text_dwms_json_get(self):
        """Test case for alpen_forecast_text_dwms_json_get

        Alpen Wettervorhersage als Text  # noqa: E501
        """
        pass

    def test_crowd_meldungen_overview_v2_json_get(self):
        """Test case for crowd_meldungen_overview_v2_json_get

        DWD Crowdwettermeldungen  # noqa: E501
        """
        pass

    def test_gemeinde_warnings_v2_en_json_get(self):
        """Test case for gemeinde_warnings_v2_en_json_get

        Gemeinde Unwetterwarnungen  # noqa: E501
        """
        pass

    def test_sea_warning_text_json_get(self):
        """Test case for sea_warning_text_json_get

        Hochsee Unwetterwarnungen als Text  # noqa: E501
        """
        pass

    def test_station_overview_extended_get(self):
        """Test case for station_overview_extended_get

        Wetterstation Daten  # noqa: E501
        """
        pass

    def test_warnings_coast_en_json_get(self):
        """Test case for warnings_coast_en_json_get

        Küsten Unwetterwarnungen (englisch)  # noqa: E501
        """
        pass

    def test_warnings_coast_json_get(self):
        """Test case for warnings_coast_json_get

        Küsten Unwetterwarnungen (deutsch)  # noqa: E501
        """
        pass

    def test_warnings_lawine_json_get(self):
        """Test case for warnings_lawine_json_get

        Alpen Wettervorhersage als Text  # noqa: E501
        """
        pass

    def test_warnings_nowcast_en_json_get(self):
        """Test case for warnings_nowcast_en_json_get

        Nowcast Warnungen (englisch)  # noqa: E501
        """
        pass

    def test_warnings_nowcast_json_get(self):
        """Test case for warnings_nowcast_json_get

        Nowcast Warnungen (deutsch)  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
