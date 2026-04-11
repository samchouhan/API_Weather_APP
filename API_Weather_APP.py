#API weather app 
#Install requests library if not already installed
#Creat a API key from openweathermap.org and replace
import requests

API_KEY = 'your_api_key_here'

WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather'
AQI_URL = 'http://api.openweathermap.org/data/2.5/air_pollution'

city = input('Enter city name: ')

# Step 1: Weather API
params = {
    'q': city,
    'appid': API_KEY,
    'units': 'metric'
}

response = requests.get(WEATHER_URL, params=params)
data = response.json()

if data['cod'] == 200:

    # Weather Data
    temperature = data['main']['temp']
    weather = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind = data["wind"]["speed"]

    # Get Coordinates
    lat = data['coord']['lat']
    lon = data['coord']['lon']

    # Step 2: AQI API
    aqi_params = {
        'lat': lat,
        'lon': lon,
        'appid': API_KEY
    }

    aqi_response = requests.get(AQI_URL, params=aqi_params)
    aqi_data = aqi_response.json()

    aqi = aqi_data['list'][0]['main']['aqi']

    # AQI Meaning
    aqi_status = {
        1: "Good 🟢",
        2: "Fair 🟡",
        3: "Moderate 🟠",
        4: "Poor 🔴",
        5: "Very Poor 🟣"
    }

    print(f"\nWeather in {city}")
    print("Temperature:", temperature, "°C")
    print("Condition:", weather)
    print("Humidity:", humidity, "%")
    print("Wind Speed:", wind, "m/s")

    print("\nAir Quality Index:", aqi, "-", aqi_status.get(aqi, "Unknown"))

else:
    print("City not found. Please check the city name.")
