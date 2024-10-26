import requests

API_KEY = '44cf86cd8cd5eaa5032828062142d64b'  # Replace with your actual API key
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']


def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    return response.json()


def convert_kelvin_to_celsius(temp_k):
    return temp_k - 273.15


def process_weather_data(city):
    data = get_weather_data(city)
    if data.get("main"):
        temp = convert_kelvin_to_celsius(data["main"]["temp"])
        feels_like = convert_kelvin_to_celsius(data["main"]["feels_like"])
        weather_condition = data["weather"][0]["main"]
        return {
            'city': city,
            'temp': temp,
            'feels_like': feels_like,
            'condition': weather_condition,
            'timestamp': data['dt']
        }
    return None
