import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Navendu Vyas")
    content = """
    Hi, I am Navendu! I am a Tech Product Manager, building awesome products using ML amd Deep Learning. 
    I have 18 years of experience and i have worked in 6 companies"""
    st.info(content)