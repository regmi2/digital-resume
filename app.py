from pathlib import Path

import streamlit as st
from PIL import Image

current_dir = Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "profilePic.png"


# GENERAL SETTINGS

page_title = "Digital Resume | Pallav Regmi"
icon = ":wave:"
name = "Pallav Regmi"
description = """
Entrepreneur, Artist & Educator working with cutting edge technology to build greater accessibility for all global citizens.
"""

email = "regmipallav@gmail.com"
socials = {
    "LinkedIn": "https://www.linkedin.com/in/pallav-regmi/",
    "GitHub": "https://github.com/regmi2",
    "Twitter": "https://twitter.com/PallavRegmi11"
}

PROJECTS = {
    "Mirch Masala Menu + Info Website": "https://www.mirchmasalamadison.com",
    "Income and Expense Tracker - Web App with NoSQL DB": "XO"
}


# set title and icon
st.set_page_config(page_title=page_title, page_icon=icon)


st.title("Pallav Regmi's Digital Resumé :wave:")


# --- LOAD CSS, PDF, PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf:
    PDFbyte = pdf.read()
    profile_pic = Image.open(profile_pic)


# ---HERO SECTION ---

col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(name)
    st.write(description)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )

    st.write(":email:", email)


# ---SOCIAL LINKS ---
st.write("#")
cols = st.columns(len(socials))
for index, (platform, link) in enumerate(socials.items()):
    cols[index].write(f"[{platform}]({link})")


# ---EXPERIENCE + QUALIFICATIONS ---

st.write("#")
st.header("Experience & Qualifications")
st.write(
    """
    - 5+ years experience building practical result-oriented tech solutions
    - 10+ years as an educator in STEM and Effective Communication skills
    - Strong programming foundations with a comprehensive, self-motivated problem solving approach to simplify and overcome complex obstacles
    - Excellent team player with effective written and verbal communication between collaborators
    """
)


# --- SKILLS ---

st.write("#")
st.header("Skills")
st.write(
    """
    - Programming: Python (Scikit-learn, Pandas, numpy, Streamlit), React, Vue.JS,  C, Java, SQL, VBA, HTML, CSS, JavaScript, Rust, Haskell
    - Natural Language: Excellent written and verbal communication in English with a focus on clarity and conciseness, fluent in Nepali, conversational in Spanish, beginner in German
    - Video: DSLR Video Camera Expert, DaVinci Resolve, Adobe Premiere Pro, Adobe After Effects, Adobe Media Encoder
    - Image & Design: Adobe Illustrator, Adobe Photoshop, Canva, Figma
    - Audio Software: Ableton Live, FL Studio, 
    - Data Visualization: PowerBI, MS Excel, Plotly
    - Modeling: Logistic Regression, Linear Regression, Decision Trees
    - Databases: Postgres, MongoDB, MySQL
    - Software/Platforms: GitHub, WordPress, SquareSpace, Wix, Visual Studio Code, Eclipse, Visual Basic, Adobe Suite, PHPMyAdmin
    """
)


# ---WORK HISTORY --

st.write("#")
st.header("Work History")
st.write("---")

# --JOB 1
st.subheader("Website, Content, and Strategy Engineer, Founder | Web Hill Tech")
st.write("11/2021 - Present")
st.write(
    """
    - built excellent rapport with clients to identify their website, content, and strategy needs for business and personal growth with atleast 20%+ revenue growth
    - led a 3 person international development team and delegated tasks effectively based on specializations of collaborators
    - established top 3 Google Ranking to increase visibility to the market
    """
)

st.subheader(
    "STEM Educator/Academic Coach | UW-Madison, Madison West High, iDTech")
st.write(" 9/2012- Present")
st.write(
    """
- Craft accessible, clear, and actionable STEM learning paths for middle school to undergrad level students
- Present challenging content in a clear and stimulating manner, ensuring comprehension for each student 
- Successfully guided multiple students to a greater than 10% increase in exam scores, on average
    """
)

st.subheader(
    "Implementation Consultant at the Puerto Rico Department of Treasury | FAST Enterprises")
st.write("10/2020 - 10/2021")
st.write(
    """
 - Maintain a jovial and professional rapport and craft questions to identify client pain points 
 - Assemble details of a COTS tax revenue management system to enhance taxpayer experience 
 - Collaborate with high-level government officials and seasoned IT professionals in crafting logic and solving client-specified problems
    """
)

st.subheader("Founder & Creative Director | ANUV")
st.write("9/2021 - Present")
st.write(
    """
    - Craft and strategize presentation of compelling content for artists in New York City, Kathmandu, & around Wisconsin
    - Provide expert input on audio, video, design, and presentation on technical softwares as well as crafting ways to overcome creative obstacles 
    """
)


# --- PROJECTS & ACCOMPLISHMENTS

st.write('#')
st.header("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
