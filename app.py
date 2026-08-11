t requests
import streamlit as st

# Configure Page
st.set_page_config(page_title="Student Management Portal", layout="centered")
st.title("🎓 Student Management Portal")

# Backend API Base URL Configuration
API_URL = st.sidebar.text_input("Backend API Base URL", value="https://batch-555-b.onrender.com")

# Navigation Menu
option = st.sidebar.selectbox(
    "Select Action",
    [
        "View All Students",
        "View Student by ID",
        "Add New Student",
        "Update Student",
        "Delete Student",
    ],
