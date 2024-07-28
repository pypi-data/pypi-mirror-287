import requests


class Weather:
    """
        Creates a Weather object getting an api_key as input
        and either a city name or lat and lon coordinates.

        Package use example:

        - Create a weather object using a city name.
        - The api key below is not guaranteed to work.
        - Get your own api key from https://openweathermap.org
        - And wait a couple of hours for the api key to be activated.
        > weather1 = Weather(api_key="9aa0a64f4ec827263fe827fdee259a61", city="Madrid")

        - Using latitude and longitude coordinates
        > weather2 = Weather(api_key="9aa0a64f4ec827263fe827fdee259a61", lat=41.1, lon=-4.1)

        - Get complete weather data for the next 12 hours.
        > weather1.next_12h()

        - Simplified data for the next 12 hours:
        > weather1.next12h_simplified()

        - Sample url to get sky condition icons:
        http://openweathermap.org/tmg/wn/10d@2x.png
    """

    def __init__(self, api_key, city=None, lat=None, lon=None):

        if city:
            url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={api_key}&units=imperial"
            r = requests.get(url)
            self.data = r.json()
        elif lat and lon:
            url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&APPID={api_key}&units=imperial"
            r = requests.get(url)
            self.data = r.json()
        else:
            raise TypeError("Provide either a city or lat and lon arguments.")
        if self.data['cod'] != '200':
            raise ValueError(self.data['message'])

    def next_12h(self):
        """
            Returns 3-hour data for the next 12 hours as a dict.
        """
        return self.data['list'][:4]

    def next_12h_simplified(self):
        """
            Returns the date, temperature, and sky condition every 3 hours
            for the next 12 hours as a tuple of tuples.
        """
        simple_data = []
        for dicty in self.data['list'][:4]:
            simple_data.append((dicty['dt_text'], dicty['main']['temp'], dicty['weather'][0]['description'],
                                dicty['weather'][0]['icon']))
        return simple_data


