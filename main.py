
import streamlit as st
import random
import string
import re

st.set_page_config(page_title="Password Meter, Generator & Saver", page_icon="🔐", layout="wide")

st.markdown("""
    <style>
    body {background-color: #f4f4f4;}
    .spd { padding: 10px; border-radius: 10px; color: blue, text: white,  box-shadow: 2px 2px 10px rgba(0,0,0,0.1);}
    .main { padding: 50px; border-radius: 20px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1);}
    .footer {position: fixed; bottom: 0; left: 50%; transform: translateX(-50%);
    width: 100%; text-align: center; padding: 10px; background: #fff; font-size: 14px; color: yellow, box-shadow: 0px -2px 5px rgba(0,0,0,0.1);}
    </style>
""", unsafe_allow_html=True)



#Saved Passwords
st.sidebar.title("🔑 Saved Passwords")
if "generate_password" not in st.session_state:
    st.session_state["generate_password"] = []




def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters 

    if use_digits:
        characters += string.digits

    if use_special:
        characters += string.punctuation
    
    return ' '.join(random.choice(characters) for _ in range(length))

st.title("🔐 Password Generator App 🔥")
st.write("This is a simple project to generate a password and trace it back to"
" the original password. ")
 

use_digits = st.checkbox("use digits")

use_special = st.checkbox("Include special characters")

# NATO Phonetic Alphabet
natophonetics = {
    "A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo", "F": "Foxtrot", "G": "Golf", "H": "Hotel",
    "I": "India", "J": "Juliett", "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar", "P": "Papa",
    "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango", "U": "Uniform", "V": "Victor", "W": "Whiskey",
    "X": "X-Ray", "Y": "Yankee", "Z": "Zulu"
}

def get_natophonetics(term):
    return ' '.join([natophonetics.get(i, i) for i in list(term.upper())])

#     with st.container():
#         password = st.text_input("Enter your password:", type="password")
#         if st.button("🔍 Check Strength", use_container_width=True):
#             if password:
#                 score, feedback = check_password_strength(password)
                
#                 if score == 4:
#                     st.success("✅ Strong Password!")
#                     if password not in st.session_state["generate_password"]:
#                         st.session_state["saved_passwords"].append(password)
#                 elif score == 3:
#                     st.warning("⚠️ Moderate Password - Consider adding more security features.")
#                     if password not in st.session_state["saved_passwords"]:
#                         st.session_state["saved_passwords"].append(password)
#                 else:
#                     st.error("❌ Weak Password - Improve it using the suggestions below.")
                
#                 for tip in feedback:
#                     st.write("- " + tip)
#             else:
#                 st.error("Please enter a password.")

if "Generate Strong Password":
    with st.container():
        length = st.slider("Select Password Length", 8, 20, 12)
        if st.button("⚡ Generate Password", use_container_width=True):
            generate_password = generate_password(length, use_digits, use_special)
            st.markdown('<div class="footer">Made by AS Developers ❤</div>', unsafe_allow_html=True)
            # st.write(f"Generated Password : `{generate_password}`")
            st.markdown(
                f"""
                <div style="padding:10px; background-color:#222; color:#0f0; border-radius:10px; font-size:18px;">
                    🔐 <b>Generated Password:</b> <code>{generate_password}</code>
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.write(f"🧠 Remember:: {get_natophonetics(generate_password)}")
            st.session_state["generate_password"].append(generate_password)
            saved_passwords = st.session_state["generate_password"]
            st.sidebar.write("Saved Passwords")
            with st.sidebar:
                for idx, saved_pw in enumerate(saved_passwords, start=1):
                    st.write(f"{idx}. `{saved_pw}`")            
            st.balloons() 


st.markdown('<div class="footer">Made by AS Developers ❤</div>', unsafe_allow_html=True)