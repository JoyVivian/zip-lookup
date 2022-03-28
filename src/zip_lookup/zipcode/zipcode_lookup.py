""" Process the zip code.

This module process the zip code got from the front end. Specifically, get the county
and population of it.

"""
import requests
from requests.auth import HTTPBasicAuth

import src.zip_lookup.utils.global_variable as g


class ZipCode():
    """ Create zipcode object and process it.

    This class create zipcode object using the given zip code and process it.
    This class provide two methods. get_county() is used to get the county of the given zip code.
    get_population() is used to get the population of this zip code.

    Args:
        zipcode (str): The zip code that is going to be processed.

    Attributes:
        zipcode (str): The zip code that is going to be processed.
    """

    def __init__(self, zipcode):
        self.zipcode = zipcode

    def get_county(self):
        """ Get the county of the given zip code.

        This method get the county of the given zip code using Zip API.
        The URL of this API is https://zipapi.us.
        The usage of this API to get county:

        .. _Request county:
        https://service.zipapi.us/zipcode/county/47858?X-API-KEY=your_api_key

        Returns:
            The string of the county if the response status is true,or None if it is failed.
        """
        response = requests.get(
            f"https://service.zipapi.us/zipcode/county/{self.zipcode}?X-API-KEY={g.API_KEY}",
            auth=HTTPBasicAuth(g.EMAIL, g.PASSWORD))

        if response.ok:
            response = response.json()
            data = response['data']
            return data['county']

        return None

    def get_population(self):
        """ Get the population if this zip code.

        This method get the population of the given zip code using Zip API.
        The URL of this API is https://zipapi.us.
        The usage of this API to get population:
        https://service.zipapi.us/population/zipcode/90210?X-API-KEY=your_api_key
        &fields=male_population,female_population

        Returns:
            The string of the population if response status is true, or None if failed.
        """
        response = requests.get(
            f"https://service.zipapi.us/population/zipcode/{self.zipcode}?X-API-KEY={g.API_KEY}",
            auth=HTTPBasicAuth(g.EMAIL, g.PASSWORD))

        if response.ok:
            response = response.json()
            data = response['data']
            return data['population']

        return None


