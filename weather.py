import requests
city = input  ("enter your city: ")
url = "https://geocoding-api.open-meteo.com/v1/search"
response = requests.get(url,params={"name": city})


location = response.json()["results"][0]
print(location)
latitude = location["latitude"]
longitude = location ["longitude"]

print("latitude:",latitude)
print("longitude:",longitude)
weather_url = "https://api.open-meteo.com/v1/forecast"

weather_response = requests.get(weather_url,params={"latitude":latitude,"longitude":longitude,"current": "temperature_2m,relative_humidity_2m"})
#print(weather_response.json())
weather_data = weather_response.json()["current"]
temperature = weather_data["temperature_2m"]
humidity = weather_data["relative_humidity_2m"]
time = weather_data["time"]
print(f"weather in {location["name"]}")
print(f"temperature= {temperature}°C")
print(f"the humidity outside is: {humidity}")
print(f"current time is {time}")

