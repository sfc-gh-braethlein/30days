import streamlit as st

import glob
import os

import pandas as pd
from PIL import Image


def update_params():
    st.query_params["challenge"] = st.session_state.day


md_files = sorted(
    [int(x.strip("Day").strip(".md")) for x in glob.glob("*.md", root_dir="content")]
)

# Logo and Navigation
col1, col2, col3 = st.columns((1, 4, 1))
with col2:
    st.image(Image.open("streamlit-logo-secondary-colormark-darktext.png"))
st.markdown("# 30 Days of Streamlit!!!!!")

days_list = [f"Day {x}" for x in md_files]

challenge = st.query_params.get("challenge")

if challenge and challenge in days_list:
    st.session_state.day = challenge

selected_day = st.selectbox(
    "Start the Challenge 👇", days_list, key="day", on_change=update_params
)

with st.expander("About the #30DaysOfStreamlit"):
    st.markdown(
        """
    The **#30DaysOfStreamlit** is a coding challenge designed to help you get started in building Streamlit apps.

    Particularly, you'll be able to:
    - Set up a coding environment for building Streamlit apps
    - Build your first Streamlit app
    - Learn about all the awesome input/output widgets to use for your Streamlit app
    """
    )

# Sidebar
st.sidebar.header("About")
st.sidebar.markdown(
    "[Streamlit](https://streamlit.io) is a Python library that allows the creation"
    " of interactive, data-driven web applications in Python."
)

st.sidebar.header("Resources")
st.sidebar.markdown(
    """
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Cheat sheet](https://docs.streamlit.io/library/cheatsheet)
- [Book](https://www.amazon.com/dp/180056550X) (Getting Started with Streamlit for Data Science)
- [Blog](https://blog.streamlit.io/how-to-master-streamlit-for-data-science/) (How to master Streamlit for data science)
"""
)

st.sidebar.header("Deploy")
st.sidebar.markdown(
    "You can quickly deploy Streamlit apps using"
    " [Streamlit Cloud](https://streamlit.io/cloud) in just a few clicks."
)

# Display content
for day in days_list:
    if selected_day == day:
        st.markdown(f"# 🗓️ {day}")
        day_key = day.replace(" ", "")
        with open(f"content/{day_key}.md", "r") as f:
            st.markdown(f.read())
        if os.path.isfile(f"content/figures/{day_key}.csv"):
            st.markdown("---")
            st.markdown("### Figures")
            df = pd.read_csv(f"content/figures/{day_key}.csv", engine="python")
            for idx in range(len(df)):
                st.image(f"content/images/{df.img[idx]}")
                st.info(f"{df.figure[idx]}: {df.caption[idx]}")
