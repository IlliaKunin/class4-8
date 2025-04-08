import streamlit as st
import secrets

api_key = st.secrets["alpha_vantage"]["api_key"]
st.write("# Class 4-8")
# Streamlit expects a `secrets.toml` file in the `.streamlit` directory.
# Ensure you have a `.streamlit/secrets.toml` file with the following format:

# .streamlit/secrets.toml
# [alpha_vantage]
# api_key = "your_actual_api_key"

# Replace "your_actual_api_key" with your actual API key.
