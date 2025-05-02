import streamlit as st
import json

from utils.sideBar import questionExamples

questions = json.load(open("./src/utils/questions.json"))

st.set_page_config(
    page_title="WorkWise MVP"
)

st.title("WorkWise MVP")
