import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "YOUR_API_KEY"
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"

weather_params = {
    "lat": "ENTER YOUR LATITUDE AS INT",
    "lon": "ENTER YOUR LONGITUDE AS INT",
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="whatsapp:YOUR_TWILIO_NUMBER",
        to="whatsapp:YOUR_WHATSAPP_PH_NO.",
    )
    print(message.status)

