import streamlit as st
import requests

st.set_page_config(
    page_title="Personal Task Manager",
    page_icon="✅",
    layout="wide"
)

st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

.task-card {
    padding: 15px;
    border-radius: 10px;
    border: 1px solid #ddd;
    margin-bottom: 10px;
}

.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

API_URL = "http://127.0.0.1:8000"

if "token" not in st.session_state:
    st.session_state.token = None

st.sidebar.title("📋 Task Manager")

menu = st.sidebar.selectbox(
    "Navigation",
    ["Register", "Login", "Dashboard"]
)

# ---------------- REGISTER ----------------

if menu == "Register":

    st.title("📝 Register")

    email = st.text_input("Email")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Register"):

        response = requests.post(
            f"{API_URL}/auth/register",
            json={
                "email": email,
                "password": password
            }
        )

        if response.status_code == 200:
            st.success("User registered successfully")
        else:
            st.error(response.json())

# ---------------- LOGIN ----------------

elif menu == "Login":

    st.title("🔐 Login")

    email = st.text_input("Email")
    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        response = requests.post(
            f"{API_URL}/auth/login",
            json={
                "email": email,
                "password": password
            }
        )

        if response.status_code == 200:

            st.session_state.token = response.json()["token"]

            st.success("Login successful")

        else:
            st.error("Invalid credentials")

# ---------------- DASHBOARD ----------------

elif menu == "Dashboard":

    if not st.session_state.token:
        st.warning("Please login first")
        st.stop()

    headers = {
        "Authorization":
        f"Bearer {st.session_state.token}"
    }

    st.sidebar.success("🟢 Logged In")

    if st.sidebar.button("Logout"):
        st.session_state.token = None
        st.rerun()

    st.title("📋 Personal Task Manager")
    st.caption("Manage your daily tasks efficiently")

    response = requests.get(
        f"{API_URL}/tasks/",
        headers=headers
    )

    tasks = []

    if response.status_code == 200:
        tasks = response.json()

    total_tasks = len(tasks)

    completed_tasks = len(
        [t for t in tasks if t["status"] == "Completed"]
    )

    pending_tasks = len(
        [t for t in tasks if t["status"] == "Pending"]
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Tasks",
        total_tasks
    )

    col2.metric(
        "Completed",
        completed_tasks
    )

    col3.metric(
        "Pending",
        pending_tasks
    )

    st.divider()

    st.subheader("➕ Create Task")

    title = st.text_input("Title")

    description = st.text_area("Description")

    priority = st.selectbox(
        "Priority",
        ["Low", "Medium", "High"]
    )

    status = st.selectbox(
        "Status",
        ["Pending", "In Progress", "Completed"]
    )

    due_date = st.date_input(
        "Due Date"
    )

    if st.button("Create Task"):

        response = requests.post(
            f"{API_URL}/tasks/",
            headers=headers,
            json={
                "title": title,
                "description": description,
                "priority": priority,
                "status": status,
                "due_date": str(due_date)
            }
        )

        if response.status_code == 200:
            st.success("Task Created")
            st.rerun()
        else:
            st.error(response.text)

    st.divider()

    st.subheader("📂 My Tasks")

    search = st.text_input(
        "🔍 Search Tasks"
    )

    status_filter = st.selectbox(
        "Filter by Status",
        [
            "All",
            "Pending",
            "In Progress",
            "Completed"
        ]
    )

    filtered_tasks = tasks

    if search:

        filtered_tasks = [
            task
            for task in filtered_tasks
            if search.lower()
            in task["title"].lower()
        ]

    if status_filter != "All":

        filtered_tasks = [
            task
            for task in filtered_tasks
            if task["status"] == status_filter
        ]

    priority_icons = {
        "Low": "🟢",
        "Medium": "🟡",
        "High": "🔴"
    }

    if not filtered_tasks:
        st.info("No tasks found")

    for task in filtered_tasks:

        icon = priority_icons.get(
            task["priority"],
            "⚪"
        )

        with st.expander(
            f"{icon} {task['title']} - {task['status']}"
        ):

            st.write(
                f"**Description:** {task['description']}"
            )

            st.write(
                f"**Priority:** {task['priority']}"
            )

            st.write(
                f"**Due Date:** {task['due_date']}"
            )

            if st.button(
                f"🗑 Delete Task {task['id']}"
            ):

                requests.delete(
                    f"{API_URL}/tasks/{task['id']}",
                    headers=headers
                )

                st.success("Task deleted")
                st.rerun()