# IMPORTS
import streamlit as st
import requests
from secret_stuff import secrets  # secret_stuff file is used to hide the api key

# Page Title
st.title("Weather App")

# API Key
api_key = secrets.get("api_key")

# User can input name of city
user_input = st.text_input("Enter city: ")

# Making a button to check the weather
if st.button("Check Weather"):
    # Condition for if user press button without entering anything in the input box
    if user_input.strip() == "":
        st.warning(
            "Please enter a real city name. Don't you dare click button without entering anything!"
        )

    else:
        st.write("Searching for weather...")

        # Get data from the url. For degrees celcius, use units = metric. For farenheit, use units = imperial.
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}"
        )
        # status code checks to see what happens to the requests for weather in HTTP
        # Status code 200 means its working successfully
        if weather_data.status_code == 200:
            st.success("Weather information retrieved!")

            # Convert JSON data into dictionary
            weather = weather_data.json()

            # Getting some weather information
            city = weather["name"]
            temperature = weather["main"]["temp"]
            humidity = weather["main"]["humidity"]
            description = weather["weather"][0]["description"]
            wind_speed = weather["wind"]["speed"]

            # Displaying the weather
            st.subheader("The Current Weather")

            st.write("City: ", city)
            st.write("Temperature: ", temperature, "°C")
            st.write("Humidity: ", humidity, "%")
            st.write("Conditions: ", description)
            st.write("Wind Speed: ", wind_speed, "mph")

        else:
            st.error("Unable to retrive weather information")
