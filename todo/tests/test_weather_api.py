from unittest import mock
from unittest.mock import Mock

from django.test import SimpleTestCase, override_settings

from todo.weather_api import OpenWeatherApi


@override_settings(OPENWEATHER_API_KEY='ABCD1234')
class OpenWeatherApiTestCase(SimpleTestCase):
    
    def test_get_api_key(self):

        self.assertEqual('ABCD1234', OpenWeatherApi.get_api_key())

    @mock.patch('todo.weather_api.requests.get')
    def test_get_data_none_parameters(self, requests_get_mock):
        expected_result = {'a': 'b'}
        
        requests_get_mock.return_value = Mock(json=Mock(return_value=expected_result))

        result = OpenWeatherApi.get_data(None)
        
        requests_get_mock.assert_called_once_with(OpenWeatherApi.URL, {'appid': 'ABCD1234'})     
        requests_get_mock.return_value.raise_for_status.assert_called_once()
        self.assertDictEqual(result, expected_result)  

    @mock.patch('todo.weather_api.requests.get')
    def test_get_data_for_location_id(self, requests_get_mock):
        location_id = 123
        expected_result = {'a': 'b'}

        requests_get_mock.return_value = Mock(json=Mock(return_value=expected_result))

        result = OpenWeatherApi.get_data_for_location_id(location_id)
        
        requests_get_mock.assert_called_once_with(OpenWeatherApi.URL, {'appid': 'ABCD1234', 'id': location_id})     
        requests_get_mock.return_value.raise_for_status.assert_called_once()
        self.assertDictEqual(result, expected_result)