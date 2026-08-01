import requests
import smtplib
import os
from dotenv import load_dotenv

MY_LATITUDE = 6.606268
MY_LONGITUDE = 3.375160
MY_EMAIL = "shalom.devtest@gmail.com"
MY_PASSWORD = "bwkwhfalwajbfrty"
load_dotenv()
api_key = os.environ.get("API_KEY")

parameters = {
    "lat": MY_LATITUDE,
    "lon": MY_LONGITUDE,
    "appid": api_key,
    "cnt": 4,
}

will_rain = False
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()["list"]
for hour in data:
    if hour["weather"][0]["id"] < 700:
        will_rain = True
if will_rain:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="shalomfadare@gmail.com",
            msg="Subject:Rain!\n\nDon't forget to step out with an umbrella, it is likely to rain.")

