import streamlit as st

# Create counter if it doesn't exist
if "count" not in st.session_state:
    st.session_state["count"] = 0

st.title("Counter App")

if st.button("Increment"):
    st.session_state["count"] += 1

st.metric(
    label="Current Count",
    value=st.session_state["count"]
)