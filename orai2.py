import requests

city = input("Įveskite miestą: ")

location_payload = {
    'name': city,
}

r_location = requests.get("https://geocoding-api.open-meteo.com/v1/search",
                          params=location_payload)

location_json = r_location.json()
latitude = location_json['results'][0]['latitude']
longitude = location_json['results'][0]['longitude']
# print(latitude, longitude)
weather_codes = {
	"0": "Clear sky",
	"1": "Mainly clear",
	"2": "Partly cloudy",
	"3": "Overcast",
	"45": "Fog",
	"48": "Depositing rime fog",
	"51": "Light drizzle",
	"53": "Moderate drizzle",
	"55": "Dense drizzle",
	"56": "Light freezing drizzle",
	"57": "Dense freezing drizzle",
	"61": "Slight rain",
	"63": "Moderate rain",
	"65": "Heavy rain",
	"66": "Light freezing rain",
	"67": "Heavy freezing rain",
	"71": "Slight snowfall",
	"73": "Moderate snowfall",
	"75": "Heavy snowfall",
	"77": "Snow grains",
	"80": "Slight rain showers",
	"81": "Moderate rain showers",
	"82": "Violent rain showers",
	"85": "Slight snow showers",
	"86": "Heavy snow showers",
	"95": "Thunderstorm",
	"96": "Thunderstorm with slight hail",
	"97": "Heavy thunderstorm",
	"99": "Thunderstorm with heavy hail"
}

weather_payload = {
    'latitude': latitude,
    'longitude': longitude,
    'hourly': ["temperature_2m", 'weather_code'],
    'forecast_days': 2,
}

r_weather = requests.get("https://api.open-meteo.com/v1/forecast",
                         params=weather_payload)
r_weather_json = r_weather.json()
days = r_weather_json['hourly']

print(days)

index = 0

while True:
    try:
        print(days['time'][index])
        print(days['temperature_2m'][index])
        print(weather_codes[str(days['weather_code'][index])])
        index += 1
    except IndexError:
        break