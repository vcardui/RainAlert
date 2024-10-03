import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
api_key = ""

account_sid = ""
auth_token = ""

weather_params = {
    #"lat": 21.832350,
    #"lon": -102.317330,
    "lat": 44.407059,
    "lon": 8.933990,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)
full_data = response.json()
rain_chance = False
for i in range(0, 12):
    weather_ID_hour = full_data['hourly'][i]['weather'][0]['id']
    print(weather_ID_hour)
    if int(weather_ID_hour) < 700:
        rain_chance = True

if rain_chance:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body = "It's going to rain today. Remember to bring an umbrella!",
        from_= "+16294683691",
        to = "+525529903445"
    )
    print(message.status)

"""
# For pythonAnywhere

import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
api_key = ""

account_sid = ""
auth_token = ""

weather_params = {
    #"lat": 21.832350,
    #"lon": -102.317330,
    "lat": 44.407059,
    "lon": 8.933990,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)
full_data = response.json()
rain_chance = False
for i in range(0, 12):
    weather_ID_hour = full_data['hourly'][i]['weather'][0]['id']
    print(weather_ID_hour)
    if int(weather_ID_hour) < 700:
        rain_chance = True

if rain_chance:
    
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body = "It's going to rain today. Remember to bring an umbrella!",
        from_= "+16294683691",
        to = "+525529903445"
    )
    print(message.status)
    
"""