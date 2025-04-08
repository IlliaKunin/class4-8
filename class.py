import streamlit as st
import secrets

api_key = st.secrets["alpha_vantage"]["api_key"]
st.write("# Class 4-8")
st.write(api_key)