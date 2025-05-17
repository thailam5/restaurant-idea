import streamlit as st
import json

from utils.sideBar import questionExamples

questions = json.load(open("./src/utils/questions.json"))

st.set_page_config(
    page_title="WorkWise MVP"
)

st.title("WorkWise MVP")

st.title("WorkWise Home Page")

st.header("Log In")

st.button("Manager Login")
st.button("Employee Login")

st.markdown("Want to get started with WorkWise? <br>[Click Here](https://www.google.com/).</br>", unsafe_allow_html=True)
