#API weather app 
#Install requests library if not already installed
#Creat a API key from openweathermap.org and replace
import requests 
API_KEY ='692dd93b5d2157415f18ff5b3ffecd4f'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
city = input('Enter city name: ')

params = {
    'q': city,
    'appid': API_KEY,
    'units': 'metric'
}
response = requests.get(BASE_URL, params=params)
data = response.json()

if data['cod'] == 200:
    temprature = data['main']['temp']
    description = data['weather'][0]['description']
    weather=data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind = data["wind"]["speed"]

    
    print("\nWeather in {}:",city)
    print("Temperature: {}°C".format(temprature))
    print("condition:",weather)
    print("Humidity: {}%".format(humidity))
    print("Wind Speed:", wind, "m/s")
else:
    print("City not found. Please check the city name and try again.")
    