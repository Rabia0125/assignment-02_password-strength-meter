# 🔐 Project 02: Password Strength Meter:

# Importing streamlit for the app:
import streamlit as st
# Importing the re library for regular expressions:
import re

# Write the title of the app:
st.title("🔐Password Strength Meter")  
# Write the subtitle of the app:
st.write("## Password Checker App")
# Write the welcome message of the app and the instructions:
st.markdown("""
### Welcome to the Password Strength Meter 
use this app and check your password strength meter
enter your password and see the result
""")

# Create a text input for the user to enter their password:
password = st.text_input("Enter your password", type ="password")

# Create a list to store the feedback:
feedback = []
# Create a variable to store the score:
score = 0

# Check if the user has entered a password:
if password:
    # Check if the password is at least 8 characters long:
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌Password should be at least 8 characters.")
    # Check if the password contains at least one uppercase and one lowercase letter
    if re.search(r'[A-Z]', password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one uppercase and one lowercase letter.")
    # Check if the password contains at least one number:
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one number.")
    # Check if the password contains at least one special character:
    if re.search(r'[!@#$%&*()_]', password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one special character.")
    # Check if the password is strong:
    if score == 4:  
        feedback.append("✅ Password is strong")
    else:
        feedback.append("🛑 Password is weak. Please make it stronger.")
    # Write the feedback to the user:
    if feedback:
        st.markdown("### Improvement Suggestions :")
        for suggestion in feedback:
            st.markdown(suggestion)
# If the user has not entered a password, write a message to the user:
else:
    st.info("Please enter a password...")


    
