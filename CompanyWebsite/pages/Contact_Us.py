import streamlit as st
import pandas as pd
from CompanyWebsite.send_email1 import send_email1

df = pd.read_csv(r'D:\Navendu\PythonProjects\pythonProject\CompanyWebsite\pages\topics.csv')
topics = df['topic'].tolist()

st.header("Contact Me")

with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    selected_topic = st.selectbox('Select a topic', topics)
    raw_message = st.text_area("Your message")
    message = f"""\
#Subject: New email from {user_email}

From:{user_email}
Topic:{selected_topic}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email1(message)
        st.info("Your email sent successfully")