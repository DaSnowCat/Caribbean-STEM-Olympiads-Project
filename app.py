# IMPORTS
import streamlit as st

## Page Navigation
pages = [
        st.Page("pages/0_Homepage.py", title="🌱 Edu-Agro"),
        st.Page("pages/1_Farming_Education.py", title="Farming Education"),
        st.Page("pages/2_Weather_App.py", title="Weather App"),
        st.Page("pages/3_AI_Chatbot.py", title="AI Chatbot"),
        st.Page("pages/4_Farm_Assessment.py", title="Farm Assessment"),
        st.Page("pages/5_Farmer_Market.py", title="Farmer Market"),
        st.Page("pages/6_References.py", title="References")
]
pg = st.navigation(pages, position="top")
pg.run()

# Setting page configuration
st.set_page_config(
    page_title="Edu-Agro",
    page_icon="🍀",
    layout="wide"
)
<<<<<<< HEAD


# MAIN HOMEPAGE


# Main title
edu_agro = "🌱 Edu-Agrooooo"
st.title(edu_agro)

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

col1, col2, col3 = st.columns(3, border=True)

with col1:
    st.subheader("Farmer Education", text_alignment="justify")
    st.write("Learn about climate-resilient farming techniques!")
    education_button = st.button("Farming Techniques")


with col2:
    st.subheader("Weather Application", text_alignment="justify")
    st.write("Get updates about the weather in your area!")
    weather_button = st.button("Weather App")

with col3:
    st.subheader("AI Assistant Chatbot", text_alignment="justify")
    st.write("Have queries? Check out our AI assitant chatbot!")
    ai_chatbot_button = st.button("AI Chatbot")


col4, col5, col6 = st.columns(3, border=True)

with col4:
    st.subheader("Farmer Recommendations", text_alignment="justify")
    st.write("Want tips and tricks on growing your crops better? Check out here!")
    assessment_button = st.button("Farm Assessment")

with col5:
    st.subheader("Farmer Market", text_alignment="justify")
    st.write("Advertise your crops on the market online! Check out here!")
    buisness_button = st.button("Farmer's Market")

with col6:
    st.subheader("Reference Page", text_alignment="justify")
    st.write("This is our reference page where we gather our data.")
    reference_button = st.button("References")


# Condition for when buttons are clicked
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

if reference_button:
    st.switch_page("pages/6_References.py")

# Making progress slowly but surely :)
=======
>>>>>>> e41d714d049936bc41b3374543eb4620839424dc
