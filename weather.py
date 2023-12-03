import sys
import requests
from datetime import datetime
from dotenv import dotenv_values

env_vars = dotenv_values('.env')
api_key = env_vars['API_KEY']

location="Dublin,ie"

def kelvin_to_celsius(temp_in_kelvin):
    temp_in_celsius = temp_in_kelvin - 273.15
    return "%.1f" % temp_in_celsius 

def timestamp_converter(timestamp):
    timestamp = datetime.fromtimestamp(timestamp)
    return timestamp.strftime("%H:%M")

def get_data(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        else:
            r.raise_for_status()
    except requests.RequestException:
        print(f"Sorry! There was an issue fetching data.")
        sys.exit(1)

url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&APPID={api_key}"
data = get_data(url)

weather = data['main']
sys = data['sys']

print(f'• Temperature: {kelvin_to_celsius(weather['temp'])}°C')
print(f'• Feels like: {kelvin_to_celsius(weather['feels_like'])}°C')
print(f'• Humidity: {weather['humidity']}%')
print(f'• Sunrise: {timestamp_converter(sys['sunrise'])}')
print(f'• Sunset: {timestamp_converter(sys['sunset'])}')