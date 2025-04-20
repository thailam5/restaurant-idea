import streamlit as st
import json

questions = json.load(open("./src/utils/questions.json"))

st.set_page_config(
    page_title="Restaurant App MVP"
)

st.title("Restaurant App")

st.markdown("<b>Possible Questions</b>", unsafe_allow_html=True)
for question in questions.keys():
    st.markdown(f"* {question}", unsafe_allow_html=True)


input = st.chat_input("Say Something")
if input:
    with st.chat_message("human"):
        st.write(input)
    with st.chat_message("ai"):
        st.write(questions.get(input))


with st.sidebar:
    st.write("Sidebar")