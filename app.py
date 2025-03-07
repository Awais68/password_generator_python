import streamlit as st
import base64
import re

st.set_page_config(page_title="Password Generator Strength Meter", page_icon="🔒", layout="wide")


# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-image: url("https://www.dashlane.com/_next/image?url=https%3A%2F%2Fripleyprd.wpengine.com%2Fwp-content%2Fuploads%2F2023%2F03%2FSafest-Ways-to-Remember-Your-Passwords-1024x765.png&w=1080&q=75");
#         background-size: fixex;
#         background-position: center;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
st.title("Password Generator Strength Meter" )
st.write("This is a simple project to generate a password and trace it back to the original password. ")


password = st.text_input("Enter your password", type="password")
score = 0
password_saved = [" "]

score = st.checkbox("Checking password strength")
st.slider = ("green : 8 ")#  : yellow: 6, red: 4
st.slider == score
if score == 8:
    st.write("Password is strong")
elif score == 6:
    st.write("Password is moderate")
st.write(score)
if len(password) < 8:
    score += 1
    st.warning("Password is too short, should be at least 8 characters")

if not password:
    st.warning("Please enter a password")
if not re.search("[a-z]", password) and not re.search("[A-Z]", password):
     st.warning("Password should contain both uppercase and lowercase letters") 
        
else:
        print("Password is green")
        score += 1

    


