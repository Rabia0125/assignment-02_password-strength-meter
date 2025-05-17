# 🔐 Project 02: Password Strength Meter:

import streamlit as st
import re

st.title("🔐Password Strength Meter")
st.write("## Password Checker App")
st.markdown("""
### Welcome to the Password Strength Meter 
use this app and check your password strength meter
enter your password and see the result
""")

password = st.text_input("Enter your password", type ="password")

feedback = []
score = 0

if password:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌Password should be at least 8 characters long")

    if re.search(r'[A-Z]', password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one uppercase and one lowercase letter")

    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one number")

    if re.search(r'[!@#$%&*()_]', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one special character")
    
    if score == 4:  
        feedback.append("✅ Password is strong")
    else:
        feedback.append("🛑 Password is weak. Please make it stronger")
    
    
    if feedback:
        st.markdown("### Improvement Suggestions")
        for suggestion in feedback:
            st.markdown(suggestion)

else:
    st.info("Please enter a password...")


    
