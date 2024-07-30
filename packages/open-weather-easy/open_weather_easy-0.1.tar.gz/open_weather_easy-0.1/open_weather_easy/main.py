# main.py
import requests

api_key = None

def city_name_to_weather_deta(name, deta):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    return (requests.get(base_url + "appid=" + api_key + "&q=" + name).json())[deta]

def cntwd(name, deta):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    return (requests.get(base_url + "appid=" + api_key + "&q=" + name).json())[deta]

def help():
    print("""
    hellow
          
    im radin

    you can use this library to make easy using open weather map

    sample code:

    import open_weather_easy

    api_key = "your api"

    print(cntwd(yourcity ,your deta))

    sample code 2:

    import open_weather_easy

    api_key = "your api"

    print(open_weather_easy(yourcity ,your deta))

    deta examples:

    “lon”: 52.3507
    “lat”: 36.4696
    “id”: 804
    “main”: “Clouds”
    “description”: “overcast clouds”
    “icon”: “04d”
    “base”: “stations”
    “temp”: 297.2
    “feels_like”: 297.36
    “temp_min”: 297.2
    “temp_max”: 297.2
    “pressure”: 1013
    “humidity”: 65
    “sea_level”: 1013
    “grnd_level”: 993
    “visibility”: 10000
    “speed”: 5.13
    “deg”: 273
    “gust”: 8.37
    “all”: 100
    “country”: “IR”
    “sunrise”: 1722216873
    “sunset”: 1722267561
    “timezone”: 12600
    “id”: 143534
    “name”: “Āmol”
    “cod”: 200
    """)
