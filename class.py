import streamlit as st


st.write("# Class 4-8")
try:
    api_key = st.secrets["api_key"]
    st.write("API Key successfully retrieved.")
except KeyError as e:
    st.error("Error: Missing or incorrect API key in secrets.")
    st.stop()

