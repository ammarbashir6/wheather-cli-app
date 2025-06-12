import os
import sys
import requests
from dotenv import load_dotenv

#load API Key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

# API endpoints
GEOCODING_URL = "http://api.openweathermap.org/geo/1.0/direct"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_coordinates(city):
    """Get the coordinates of a city."""
    params = {
        "q" : city,
        "appid" : API_KEY,
        "limit" : 1
    }
    try:
        response = requests.get(GEOCODING_URL, params=params)
        response.raise_for_status()
        data = response.json()
        if not data:
            print(f"Error: City '{city}' Not Found" )
            sys.exit(1)
        return data[0]["lat"], data[0]['lon']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching coordinates for city '{city}': {e}")
        sys.exit(1)

def get_weather(lat, lon):
    params = {
        "lat": lat,
        "lon": lon,
        "appid" : API_KEY,
        "units": "metric",
        "exclude" : "minutely, hourly, alerts"
     }
    
    try:
        response = requests.get(WEATHER_URL, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        sys.exit(1)
    
def display_weather(data):
    if data["cod"] != 200:
        print(f"Error: {data['message']}")
        return

    city = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"].title()
    wind_speed = data["wind"]["speed"]

        # Display formatted output
    print(f"\nWeather in {city}, {country}:")
    print(f"• Temperature: {temp}°C (Feels like {feels_like}°C)")
    print(f"• Humidity: {humidity}%")
    print(f"• Wind: {wind_speed} m/s")
    print(f"• Conditions: {description}\n")


def main():
    if len(sys.argv) < 2:
        print("Usage: python weather.py <city_name>")
        print("Example: python weather.py London")
        sys.exit(1)
    
    # Combine arguments into city name
    city = " ".join(sys.argv[1:])
    
    # Get coordinates then weather
    lat, lon = get_coordinates(city)
    weather_data = get_weather(lat, lon)
    display_weather(weather_data)


if __name__ == "__main__":
    main()