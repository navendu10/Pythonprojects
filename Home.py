"""Portfolio home page: a Streamlit app that showcases my Python projects.

Run from the repository root with:  streamlit run Home.py
The list of projects is driven by ``data.csv`` (columns: title;description;url;image).
"""

from pathlib import Path

import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).parent
IMAGES_DIR = BASE_DIR / "images"
PROJECTS_PER_LEFT_COLUMN = 10  # first N projects go left, the rest go right


def render_projects(projects):
    """Draw each project as a header, description, screenshot and source link."""
    for _, row in projects.iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(str(IMAGES_DIR / row["image"]))
        st.write(f"[Source Code]({row['url']})")


st.set_page_config(layout="wide")

# --- Intro section -------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    st.image(str(IMAGES_DIR / "photo.jpg"))

with col2:
    st.title("Navendu Vyas")
    intro = (
        "Hi, I am Navendu! I am a Tech Product Manager, building awesome "
        "products using ML and Deep Learning. I have 18 years of experience "
        "and I have worked in 6 companies."
    )
    st.info(intro)

st.write(
    "Below you can find some of the apps I have built in Python. "
    "Feel free to contact me!"
)

# --- Project grid --------------------------------------------------------
df = pd.read_csv(BASE_DIR / "data.csv", sep=";")

col3, _spacer, col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    render_projects(df[:PROJECTS_PER_LEFT_COLUMN])

with col4:
    render_projects(df[PROJECTS_PER_LEFT_COLUMN:])
