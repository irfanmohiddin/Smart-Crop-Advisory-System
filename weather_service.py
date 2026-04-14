# weather_service.py
import requests
from datetime import datetime


class WeatherService:
    def __init__(self, api_key):
        """
        Initialize weather service with API key
        Get your free API key from: https://openweathermap.org/api
        """
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather_by_city(self, city_name):
        """Get current weather for a city"""
        try:
            params = {
                'q': city_name,
                'appid': self.api_key,
                'units': 'metric'  # Celsius
            }

            print(f"Fetching weather data for {city_name}...")
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()

            # Extract weather information
            weather_info = {
                'temperature': round(data['main']['temp'], 1),
                'humidity': data['main']['humidity'],
                'rainfall': data.get('rain', {}).get('1h', 0) * 30,  # Monthly estimate
                'description': data['weather'][0]['description'],
                'city': data['name'],
                'country': data['sys']['country'],
                'wind_speed': data['wind']['speed'],
                'pressure': data['main']['pressure']
            }

            print(f"✓ Weather data retrieved successfully!")
            return weather_info

        except requests.exceptions.HTTPError as e:
            if response.status_code == 404:
                print(f"❌ City '{city_name}' not found!")
                return None
            elif response.status_code == 401:
                print(f"❌ Invalid API key! Please check your API key.")
                return None
            else:
                print(f"❌ HTTP Error: {e}")
                return None

        except requests.exceptions.ConnectionError:
            print("❌ Connection error! Please check your internet connection.")
            return None

        except requests.exceptions.Timeout:
            print("❌ Request timeout! Server took too long to respond.")
            return None

        except Exception as e:
            print(f"❌ Error fetching weather: {e}")
            return None

    def get_weather_by_coordinates(self, lat, lon):
        """Get weather by latitude and longitude"""
        try:
            params = {
                'lat': lat,
                'lon': lon,
                'appid': self.api_key,
                'units': 'metric'
            }

            print(f"Fetching weather data for coordinates ({lat}, {lon})...")
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()

            data = response.json()

            weather_info = {
                'temperature': round(data['main']['temp'], 1),
                'humidity': data['main']['humidity'],
                'rainfall': data.get('rain', {}).get('1h', 0) * 30,
                'description': data['weather'][0]['description'],
                'city': data['name'],
                'country': data['sys']['country']
            }

            print(f"✓ Weather data retrieved successfully!")
            return weather_info

        except Exception as e:
            print(f"❌ Error fetching weather: {e}")
            return None


# Test the weather service
if __name__ == "__main__":
    print("=" * 60)
    print("WEATHER SERVICE TEST")
    print("=" * 60)

    # IMPORTANT: Replace with your actual API key from OpenWeatherMap
    API_KEY = "8507423c7e317466efc6d15d508e0739"  # ← PUT YOUR API KEY HERE

    if API_KEY == "YOUR_API_KEY_HERE":
        print("\n⚠️  WARNING: Please replace 'YOUR_API_KEY_HERE' with your actual API key!")
        print("Get your free API key from: https://openweathermap.org/api")
    else:
        weather = WeatherService(API_KEY)

        # Test with different cities
        print("\n" + "-" * 60)
        print("Testing: Delhi, India")
        print("-" * 60)
        result = weather.get_weather_by_city("Delhi")

        if result:
            print(f"\n🌍 City: {result['city']}, {result['country']}")
            print(f"🌡️  Temperature: {result['temperature']}°C")
            print(f"💧 Humidity: {result['humidity']}%")
            print(f"🌧️  Estimated Monthly Rainfall: {result['rainfall']} mm")
            print(f"☁️  Description: {result['description'].title()}")
            print(f"💨 Wind Speed: {result['wind_speed']} m/s")
            print(f"📊 Pressure: {result['pressure']} hPa")

        # Test another city
        print("\n" + "-" * 60)
        print("Testing: Mumbai, India")
        print("-" * 60)
        result2 = weather.get_weather_by_city("Mumbai")

        if result2:
            print(f"\n🌍 City: {result2['city']}, {result2['country']}")
            print(f"🌡️  Temperature: {result2['temperature']}°C")
            print(f"💧 Humidity: {result2['humidity']}%")
            print(f"☁️  Description: {result2['description'].title()}")