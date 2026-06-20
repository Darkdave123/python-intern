import streamlit as st

# Create session state variable if it doesn't exist
if "name" not in st.session_state:
    st.session_state["name"] = ""

st.title("Greeting App")

name = st.text_input(
    "Enter your name",
    value=st.session_state["name"]
)

if st.button("Greet"):
    st.session_state["name"] = name
    st.success(f"Hello, {name}!")