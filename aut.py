import streamlit as st
from home import home_page
from data import data_page
from predict import predict_page
from dashboard import dashboard_page

# Authentication page
def authenticate():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        login_form()
    else:
        # Once authenticated, run the main app
        home_page()

# Define the login page
def login_form():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "admin" and password == "password":
            st.session_state.authenticated = True
            st.rerun()  # Rerun the script to show the main app
        else:
            st.error("Invalid credentials")

# Main app page
def main_app():
    # Creating a sidebar for navigation
    st.sidebar.title("Navigator")
    st.sidebar.write("Use this to select between pages")
    page = st.sidebar.selectbox("Navigate", ["Home", "Data", "Predict", "Dashboard"])

    # Assigning to the appropriate pages based on sidebar selection
    if page == "Home":
        home_page()
    elif page == "Data":
        data_page()
    elif page == "Predict":
        predict_page()
    elif page == "Dashboard":
        dashboard_page()

if __name__ == "__main__":
    authenticate()
