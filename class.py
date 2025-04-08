import streamlit as st
import secrets


st.write("# Class 4-8")
try:
    api_key = st.secrets["alpha_vantage"]["api_key"]
    st.write("API Key successfully retrieved.")
except KeyError as e:
    st.error("Error: Missing or incorrect API key in secrets.")
    st.stop()

