from unittest.mock import Mock, patch
import sys

sys.path.append("..")


from nose.tools import assert_list_equal, assert_is_none, assert_equal


from src.zip_lookup.zipcode.zipcode_lookup import ZipCode


class TestZipCode(object):
    @classmethod
    def setup_class(cls):
        cls.mock_get_patcher = patch('src.zip_lookup.zipcode.zipcode_lookup.requests.get')
        cls.mock_get = cls.mock_get_patcher.start()

    @classmethod
    def teardown_class(cls):
        cls.mock_get_patcher.stop()

    def test_get_county_when_response_is_ok(self):
        self.mock_get.return_value.ok = True

        falk_response = {
            "status": "true",
            "data": {
                "zipcode": "02118",
                "county": [
                    "Suffolk"
                ]
            }
        }

        self.mock_get.return_value = Mock()
        self.mock_get.return_value.json.return_value = falk_response

        response = ZipCode("02118").get_county()
        assert_list_equal(response, falk_response['data']['county'])

    def test_get_county_when_response_is_not_ok(self):
        self.mock_get.return_value.ok = False

        response = ZipCode("02118").get_county()

        assert_is_none(response)

    def test_get_population_when_response_is_ok(self):
        self.mock_get.return_value.ok = True

        falk_response = {
            "status": "true",
            "data": {
                "population": "26498"
            }
        }

        self.mock_get.return_value = Mock()
        self.mock_get.return_value.json.return_value = falk_response

        response = ZipCode("02118").get_population()
        assert_equal(response, falk_response['data']['population'])

    def test_get_population_when_response_is_not_ok(self):
        self.mock_get.return_value.ok = False

        response = ZipCode("02118").get_population()

        assert_is_none(response)
