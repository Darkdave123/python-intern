import streamlit as st
import requests

# -------------------
# Session State Setup
# -------------------

st.session_state.setdefault("token", None)
st.session_state.setdefault("email", None)

# -------------------
# Dashboard
# -------------------

if st.session_state["token"]:

    st.title("Dashboard")

    st.success(
        f"Welcome {st.session_state['email']}"
    )

    if st.button("Logout"):

        st.session_state["token"] = None
        st.session_state["email"] = None

        st.rerun()

# -------------------
# Login Page
# -------------------

else:

    st.title("Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        try:

            response = requests.post(
                "http://127.0.0.1:8000/auth/login",
                json={
                    "email": email,
                    "password": password
                }
            )

            if response.status_code == 200:

                data = response.json()

                st.session_state["token"] = data["token"]
                st.session_state["email"] = email

                st.rerun()

            else:

                st.error(
                    response.json()["detail"]
                )

        except requests.exceptions.ConnectionError:

            st.error(
                "FastAPI server is not running"
            )