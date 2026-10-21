# IMPORTS
import streamlit as st


# MAIN HOMEPAGE

# Main title
st.title("🌱 Edu-Agro")

# Edu-Agro tagline
st.write("Building Innovation and Climate Resilience")

# Some welcome message
st.header("Welcome to Edu-Agro! Where you learn a lot")

st.write(
    "Are you a small-scale farmer looking to help your crops be at the optimal level?"
)
st.write("Well you've come to the right place!")

# Header for What is Edu-Agro is all about
st.header("What is Edu-Agro?")
st.write(
    "Edu-Agro is an AI-powered agricultural\n"
    " application designed to empower farmers across Jamaica and the wider Caribbean by promoting climate-resilient farming practices. \n"
    "The application educates farmers about sustainable agricultural techniques, provides real-time weather updates and climate alerts, \n"
    "and offers personalized farming recommendations based on soil type, terrain, and environmental conditions."
)


# Buttons

st.header("Check Out What We Offer")

education_button = st.button("Farming Techniques")
weather_button = st.button("Weather App")
ai_chatbot_button = st.button("AI Chatbot")
assessment_button = st.button("Farm Assessment")
buisness_button = st.button("Farmer's Market")

if education_button:
    st.switch_page("pages/1_Farming_Education.py")

if weather_button:
    st.switch_page("pages/2_Weather_App.py")

if ai_chatbot_button:
    st.switch_page("pages/3_AI_Chatbot.py")

if assessment_button:
    st.switch_page("pages/4_Farm_Assessment.py")

if buisness_button:
    st.switch_page("pages/5_Farmer_Market.py")
