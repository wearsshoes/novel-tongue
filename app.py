"""
Main application script for the app.
"""

import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Hello! Welcome to Streamlit! 👋")

FILE_DIR = "/workspace/novel-tongue/notebooks/alice_in_wonderland"

c1_en = open(f"{FILE_DIR}/c1_en.txt", "r", encoding="UTF-8").read()
c1_es = open(f"{FILE_DIR}/c1_es.txt", "r", encoding="UTF-8").read()

st.columns([c1_en, c1_es])
