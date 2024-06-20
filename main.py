import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Navendu Vyas")
    content = """
    Hi, I am Navendu! I am a Tech Product Manager, building awesome products using ML and Deep Learning. 
    I have 18 years of experience and i have worked in 6 companies"""
    st.info(content)

content2 = """
Below you can find some of the apps i have built in Python. Feel free to contact me!"""

st.write(content2)

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
