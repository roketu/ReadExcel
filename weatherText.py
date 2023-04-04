import requests

# Define the API endpoint and parameters
# endpoint = "http://api.openweathermap.org/data/2.5/weather"
endpoint = "http://api.openweathermap.org/data/2.5/forecast/daily"
lat = "139.44"
lon = "35.39"
cnt = 16

city = "London"
country_code = "uk"
app_id = "ad9f465e39291bc68fa1823751b1190e"

# Make the API request
# response = requests.get(f"{endpoint}?q={city},{country_code}&appid={app_id}")
response = requests.get(f"{endpoint}?lat={lat}&lon={lon}&cnt={cnt}&appid={app_id}")

# Get the response data
response_data = response.json()

# Get the temperature
temperature = response_data["main"]["temp"]
print(f"Temperature in {city}: {temperature} Kelvin")