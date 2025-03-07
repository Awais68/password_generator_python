
import streamlit as st
import random
import string


st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://www.dashlane.com/_next/image?url=https%3A%2F%2Fripleyprd.wpengine.com%2Fwp-content%2Fuploads%2F2023%2F03%2FSafest-Ways-to-Remember-Your-Passwords-1024x765.png&w=1080&q=75");
        background-size: fixex;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters 

    if use_digits:
        characters += string.digits

    if use_special:
        characters += string.punctuation
    
    return ' '.join(random.choice(characters) for _ in range(length))

st.title("Password Generator")
st.write("This is a simple project to generate a password and trace it back to"
" the original password. ")
 
length = st.slider("Length of password", min_value=8, max_value=24, value=12)

use_digits = st.checkbox("use digits")

use_special = st.checkbox("INclude special characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generated Password : `{password}`")


st.write("________--------_________")
st.write("Made with ❤️ by AS Develpers")