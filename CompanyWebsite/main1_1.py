import streamlit as st
import pandas as pd
import os

# Set webpage layout to wide
st.set_page_config(layout="wide")

# Add a header and some other text
st.header("The Best Company")
st.write("""
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit 
in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui 
officia deserunt mollit anim id est laborum.
""")
st.subheader("Our Team")

# Prepare the columns
col1, col2, col3 = st.columns(3)

# Read the CSV file
df = pd.read_csv(r'D:\Navendu\PythonProjects\pythonProject\CompanyWebsite\data.csv')

def display_team_members(column, members):
    for _, row in members.iterrows():
        # Add member's first and last names
        column.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        # Add member's role in the company
        column.write(row["role"])
        # Add member's photo with error handling
        image_path = os.path.join("D:/Navendu/PythonProjects/pythonProject/CompanyWebsite/images", row["image"])
        if os.path.exists(image_path):
            column.image(image_path)
        else:
            column.write("Image not available")

# Add content to the first column
with col1:
    display_team_members(st, df[:4])

# Add content to the second column
with col2:
    display_team_members(st, df[4:8])

# Add content to the third column
with col3:
    display_team_members(st, df[8:])

# Run the script with streamlit
if __name__ == "__main__":
    os.system(r"D:\Navendu\PythonProjects\pythonProject\.venv\Scripts\python.exe -m streamlit run D:\Navendu\PythonProjects\pythonProject\CompanyWebsite\main1.py")
