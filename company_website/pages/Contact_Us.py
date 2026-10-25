"""Contact page for the company website demo: emails a topic-tagged message."""

from pathlib import Path

import pandas as pd
import streamlit as st

from send_email import send_email

TOPICS_FILE = Path(__file__).parent / "topics.csv"
topics = pd.read_csv(TOPICS_FILE)["topic"].tolist()

st.header("Contact Us")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    selected_topic = st.selectbox("Select a topic", topics)
    raw_message = st.text_area("Your message")
    submitted = st.form_submit_button("Submit")

if submitted:
    if "@" not in user_email or not raw_message.strip():
        st.error("Please enter a valid email address and a message.")
    else:
        try:
            send_email(
                subject=f"[{selected_topic}] New email from {user_email}",
                body=f"From: {user_email}\nTopic: {selected_topic}\n\n{raw_message}",
                reply_to=user_email,
            )
        except Exception as error:
            st.error(f"Sorry, your message could not be sent ({error}).")
        else:
            st.info("Your email was sent successfully.")
