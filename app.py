# Import the Streamlit library
import streamlit as st

# Configure the application
st.set_page_config(page_title="Climate-Smart Farming", page_icon="🌱", layout="wide")

# Main heading
st.title("🌱 Climate-Smart Farming Assistant")

# Introduction
st.write(
    "Empowering Caribbean farmers through " "climate-resilient agricultural practices."
)

# Create a divider
st.divider()

# Welcome message
st.header("Welcome, Farmer! 👨‍🌾")

st.write(
    "Our application helps farmers discover "
    "sustainable agricultural techniques and "
    "prepare for climate-related challenges."
)

# Create three columns
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🌿 Learn")
    st.write("Explore climate-resilient farming techniques.")

with col2:
    st.subheader("🌦️ Weather")
    st.write("Check weather forecasts and climate information.")

with col3:
    st.subheader("🤖 AI Assistant")
    st.write("Get personalized agricultural guidance.")

# Interactive button
st.divider()

if st.button("Get Started 🌱"):
    st.success("Welcome! Your farming journey begins here.")
