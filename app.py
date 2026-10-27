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
    page_title="Edu Agro",
    page_icon="🍀",
    layout="wide"
)
