from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "machels-cv.docx"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Machel Odhiambo"
PAGE_ICON = ":wave:"
NAME = "Machel Odhiambo"
DESCRIPTION = """
Software Developer.
"""
EMAIL = "machelodhiambo@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/gabrielmachelo/",
    "GitHub": "https://github.com/chell0",
    "Twitter": "https://twitter.com/CodeWithChelloh"
}
PROJECTS = {
    "🏆 Agency Website - Website for a web development company": "https://www.kazifiti.com",
    "🏆 Cafe Menu - Showcasing a cafe's menu": "https://chell0.github.io/cafe-menu/",
    "🏆 Tribute Page - Giving tribute to a great leader": "https://Chell0.github.io/tribute-page"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)



# --- LOAD CSS, DOCX & PROFILE PHOTO ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as doc_file:
    DOCbyte = doc_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
    

