import requests
from django.conf import settings


class OpenWeatherApi:
    URL = "http://api.openweathermap.org/data/2.5/weather"

    @staticmethod
    def get_api_key():
        return settings.OPENWEATHER_API_KEY

    @classmethod
    def get_data(cls, request_params):
        """Gets data from OpenWeatherAPI for different requests parameters
        https://openweathermap.org/current
        """
        if isinstance(request_params, dict):
            request_params["appid"] = cls.get_api_key()
        else:
            request_params = {"appid": cls.get_api_key()}

        response = requests.get(cls.URL, request_params)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()

        return response.json()

    @classmethod
    def get_data_for_location_id(cls, location_id):
        """Gets data for location id"""

        parameters = {"id": location_id}
        data = cls.get_data(parameters)
        return data

    @classmethod
    def get_current_weather_condition_for_location_id(cls, location_id):
        """Gets current weather condition for location
        https://openweathermap.org/weather-conditions
        It turned out not to meet task requirements
        """
        weather = cls.get_data_for_location_id(location_id).get("weather")
        return weather.get("main").lower()
