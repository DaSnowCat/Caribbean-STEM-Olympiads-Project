# IMPORTS
import streamlit as st
import requests
from secret_stuff import secrets

# Page Title
st.title("Weather App")

# API Key
api_key = secrets.get("api_key")

user_input = input("Enter city: ")
# print(user_input)

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}"
)
# print(weather_data.status_code)

# print(weather_data.json())

if weather_data.json()["cod"] == "404":
    print("No City Found")
else:
    weather = weather_data.json()["weather"][0]["main"]
    temp = round(weather_data.json()["main"]["temp"])

    print((f"The weather in {user_input} is: {weather}"))
    print(f"The temperature in {user_input} is: {temp} degrees farenheit")

# st.write("This is it ", user_input)
