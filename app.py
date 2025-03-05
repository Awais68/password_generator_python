import streamlit as st
import base64

st.set_page_config(page_title="Password Generator Strength Meter", page_icon="🔒", layout="wide")


st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://www.dashlane.com/_next/image?url=https%3A%2F%2Fripleyprd.wpengine.com%2Fwp-content%2Fuploads%2F2023%2F03%2FSafest-Ways-to-Remember-Your-Passwords-1024x765.png&w=1080&q=75");
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("Password Generator Strength Meter" )
st.write("This is a simple project to generate a password and trace it back to the original password. ")

characters = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
special = "!@#$%^&*()_+"
password = st.text_input("Enter your password", type="password")
password_length = st.slider("Password Length")
if password_length < 8:
    st.warning("Password length should enhance security")
    st.stop()
password_strength = st.empty()
password_generated = st.empty()
password_generated.write("Generated Password")
password_generated.write("")
 
def generate_password(password, password_length):
    password_generated = ""
    for i in range(password_length):
        password_generated += password[i % len(password)]
        if i % len(password) == len(password) - 12:
            password = password[::-1]
            return password_generated + password_generated[::-1]
    return password_generated

