import streamlit as st

st.set_page_config(
    page_title="Restaurant App MVP"
)

st.title("Restaurant App")


input = st.chat_input("Say Something")
if input:
    with st.chat_message("human"):
        st.write(input)
    with st.chat_message("ai"):
        st.write("Received")


with st.sidebar:
    st.write("Sidebar")