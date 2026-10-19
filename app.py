# Import Streamlit
import streamlit as st


# -----------------------------
# EDU-AGRO HOMEPAGE
# -----------------------------

# Main title
st.title("🌱 Edu-Agro")

# Application slogan
st.write("Growing Knowledge, Cultivating Resilience.")

# Welcome message
st.header("Welcome to Edu-Agro!")

st.write("Your smart agricultural companion for climate-resilient farming.")

st.write("Explore our features using the sidebar on the left.")


# -----------------------------
# OUR FEATURES
# -----------------------------

st.header("🌿 Explore Our Features")

# Divide the screen into two columns
col1, col2 = st.columns(2)


# First column
with col1:
    st.subheader("🌾 Farming Education")
    st.write("Learn sustainable farming techniques.")

    st.subheader("🌤️ Weather Updates")
    st.write("Stay informed about weather conditions.")

    st.subheader("🤖 AI Assistant")
    st.write("Ask questions about agriculture.")


# Second column
with col2:
    st.subheader("🌱 Farm Assessment")
    st.write("Discover suitable farming techniques.")

    st.subheader("🎮 Virtual Farm")
    st.write("Learn through an interactive farming game.")

    st.subheader("🛒 Marketplace")
    st.write("Connect farmers with prospective buyers.")
