#!/usr/bin/env python3

import requests_cache
from timezonefinder import TimezoneFinder
import tempfile

from bs4 import BeautifulSoup
from latest_user_agents import get_random_user_agent

BASEURL = 'https://www.airnav.com/airport'


class AirNavAirports:
    def __init__(self):
        """
        Initializes a new instance of the AirNavAirports class.

        This constructor sets up the necessary attributes for the class. It creates a new instance of the CachedSession class from the requests_cache module, passing in the path to the cache file as a parameter. It also initializes the TimezoneFinder attribute.

        Parameters:
            None

        Returns:
            None
        """
        self.tempdir = tempfile.gettempdir()  # platform independent way to find a safe place to maintain a cache file
        self.session = requests_cache.CachedSession(f'{self.tempdir}/airportinfo-cache')
        self.tzf = TimezoneFinder()

    def lookup_airport(self, code):
        """
        Lookup an airport by its ICAO code via AirNav.com
        note, this uses requests caching to prevent unnecessary traffic to AirNav.com
        this data doesn't change.

        Args:
            code (str): The ICAO code of the airport to lookup.

        Returns:
            dict: A dictionary containing information about the airport. The dictionary has the following keys:
                - 'name' (str): The full name of the airport.
                - 'short_name' (str): The short name of the airport.
                - 'city' (str): The city of the airport.
                - 'state' (str): The city of the airport.
                - 'faa_identifier' (str): The FAA identifier of the airport.
                - 'lat' (float): The latitude of the airport.
                - 'lon' (float): The longitude of the airport.
                - 'timzone' (str): The timezone of the airport.
                - 'ele_ft' (float): The elevation of the airport in feet.
                - 'ele_m' (float): The elevation of the airport in meters.
                - 'zip_code' (str): The zip code of the airport.
                - 'from_cache' (bool): True if the request was made from the cache, False otherwise.
        """
        url = f"{BASEURL}/{code}"
        response = self.session.get(url, headers={'User-Agent': get_random_user_agent()})
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find_all('table')
        desc, name, name_short = self.name_and_city(table[3])
        city, state, country = desc.split(', ')
        ele_ft, ele_m, faa_identiier, lat, lon, zip_code = self.location_info(table[6].find('table'))

        result = {'name': name, 'short_name': name_short, 'desc': desc,
                  'city': city, 'state': state, 'country': country,
                  'faa_identifier': faa_identiier, 'lat': lat, 'lon': lon,
                  'timzone': self.tzf.timezone_at(lng=lon, lat=lat),
                  'ele_ft': ele_ft, 'ele_m': ele_m, 'zip_code': zip_code,
                  'from_cache': response.from_cache
                  }
        result['city'] = city
        result['state'] = state
        return result

    def location_info(self, location_table):
        rows = location_table.find_all('tr')
        faa_identiier = rows[0].find_all('td')[1].text
        latlon = rows[1].find_all('td')[1].find_all('br')[1].find_next(text=True)
        latstr, lonstr = latlon.split(',')
        lat = float(latstr)
        lon = float(lonstr)
        elevationstr = rows[2].find_all('td')[1].text
        ftstr, mstr = elevationstr.split(' / ')
        ele_ft = float(ftstr.replace(' ft.', ''))
        ele_m = float(mstr.replace(' m', '').replace(' (surveyed)', ''))
        zip_code = rows[6].find_all('td')[1].text
        return ele_ft, ele_m, faa_identiier, lat, lon, zip_code

    def name_and_city(self, table):
        cells = table.find_all('td')
        name = cells[1].find('font').find_next(string=True)
        name_short = name
        for attr in ['International', 'Airport']:
            name_short = name_short.replace(f' {attr}', '').strip()
        desc = cells[1].find('br').find_next(string=True)
        return desc, name, name_short
