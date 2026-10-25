"""Contact form page: emails the visitor's message to the site owner."""

import streamlit as st

from send_email import send_email

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your message")
    submitted = st.form_submit_button("Submit")

if submitted:
    # Minimal validation so we don't send empty emails.
    if "@" not in user_email or not raw_message.strip():
        st.error("Please enter a valid email address and a message.")
    else:
        try:
            send_email(
                subject=f"New email from {user_email}",
                body=f"From: {user_email}\n\n{raw_message}",
                reply_to=user_email,
            )
        except Exception as error:  # SMTP / configuration problems
            st.error(f"Sorry, your message could not be sent ({error}).")
        else:
            st.info("Your email was sent successfully.")
