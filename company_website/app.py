"""Company website demo: a Streamlit page with a team directory.

Run from the repository root with:  streamlit run company_website/app.py
Team members are read from ``data.csv`` (columns: first name, last name, role, image).
"""

from pathlib import Path

import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).parent
IMAGES_DIR = BASE_DIR / "images"

# How many team members to show per column (3 columns, remainder goes last).
SLICES = [slice(0, 4), slice(4, 8), slice(8, None)]


def display_team_members(column, members):
    """Render name, role and photo for each member inside the given column."""
    for _, row in members.iterrows():
        column.subheader(f'{row["first name"].strip().title()} {row["last name"].strip().title()}')
        column.write(row["role"])

        image_path = IMAGES_DIR / row["image"]
        if image_path.exists():
            column.image(str(image_path))
        else:
            column.write("Image not available")


st.set_page_config(layout="wide")

st.header("The Best Company")
st.write(
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
    quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
    consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
    cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat
    non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    """
)
st.subheader("Our Team")

df = pd.read_csv(BASE_DIR / "data.csv")

for column, rows in zip(st.columns(3), SLICES):
    with column:
        display_team_members(st, df.iloc[rows])
