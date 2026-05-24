import requests
import random
from twilio.rest import Client
import os



OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

api_parameters = {
    "lat": 50.447731,
    "lon": 30.542721,
    "appid": api_key,
    "cnt": 4,
}
r = requests.get(OWM_Endpoint, params=api_parameters)
r.raise_for_status()
weather_data = r.json()


will_rain = False
id_list = [n["weather"][0]["id"] for n in weather_data["list"]]
for i in id_list:
    if int(i) < 700:
        will_rain = True
        break
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="+380 73 021 2948",
        from_="+13366066233",
        body="It's going to rain today. Remember to bring an umbrella.")

    print(message.status)
