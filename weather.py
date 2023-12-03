import requests
from datetime import datetime
from dotenv import dotenv_values

# Load environment variables from .env file
env_vars = dotenv_values('.env')

# Access the API key
api_key = env_vars['API_KEY']

LOCATION="Drogheda,ie"
# Endpoint:
# - Please, use the endpoint api.openweathermap.org for your API calls
# - Example of API call:
# api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=1be0d5d55f890df8e97dffe93050bf9a

def kelvin_to_celsius(temp_in_kelvin):
    temp_in_celsius = temp_in_kelvin - 273.15
    return "%.1f" % temp_in_celsius 

def timestamp_converter(timestamp):
    timestamp = datetime.fromtimestamp(timestamp)
    return timestamp.strftime("%H:%M")

r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={LOCATION}&APPID={api_key}")
data = r.json()

weather = data['main']
sys = data['sys']

print(f'• Temperature: {kelvin_to_celsius(weather['temp'])}°C')
print(f'• Feels like: {kelvin_to_celsius(weather['feels_like'])}°C')
print(f'• Humidity: {weather['humidity']}%')
print(f'• Sunrise: {timestamp_converter(sys['sunrise'])}')
print(f'• Sunset: {timestamp_converter(sys['sunset'])}')