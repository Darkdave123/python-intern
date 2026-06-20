import streamlit as st

st.title("Registration Form")

with st.form("user_form"):

    name = st.text_input("Name")

    email = st.text_input("Email")

    age = st.number_input(
        "Age",
        min_value=0
    )

    submitted = st.form_submit_button(
        "Submit"
    )

if submitted:

    if age <= 0:
        st.error(
            "Age must be greater than 0"
        )

    elif "@" not in email:
        st.error(
            "Email must contain @"
        )

    else:
        st.success(
            f"Welcome {name}!"
        )

        st.write(
            f"Email: {email}"
        )

        st.write(
            f"Age: {age}"
        )