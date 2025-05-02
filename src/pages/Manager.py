import streamlit as st
import streamlit_calendar as stc
import json
from utils.sideBar import questionExamples

conversation = True

st.set_page_config(
    page_title="Manager View"
)

if "messages" not in st.session_state:
    st.session_state["messages"] = []

st.title("WorkWise Manager")

questions = json.load(open("./src/utils/questions.json"))

questionExamples(questions=questions)

with st.sidebar:
    st.write("Sidebar")

body, chat = st.columns([3,2])

st.markdown("""## Updates
* Update 1
* Update 2
* Update 3""", unsafe_allow_html=True)

stc.calendar()
st.markdown("## Notifications", unsafe_allow_html=True)

if input := st.chat_input("Enter your messsage"):

        
    st.session_state["messages"].append(
        {
            "role": "user",
            "content": input,
        }
    )
    st.session_state["messages"].append(
        {
            "role": "assistant",
            "content": questions.get(input)
        }
    )
    
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.write(message["content"])
