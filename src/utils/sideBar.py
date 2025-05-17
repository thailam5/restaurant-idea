import streamlit as st
import json

def questionExamples(questions: json):

    with st.sidebar:
        st.title("Example Chatbot Input Questions")
        for question in questions.keys():
            st.markdown(f"* {question}", unsafe_allow_html=True)