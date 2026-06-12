# stream_app.py

import streamlit as st
import pandas as pd
import os
import sys
import tempfile

# ---------------------------------------------------
# Fix Import Path
# ---------------------------------------------------

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

# ---------------------------------------------------
# Backend Imports
# ---------------------------------------------------

from backend.parser import extract_text

from backend.recommendation import (

    semantic_match_score,

    extract_skills,

    recommend_skills,

    generate_feedback,

    resume_strength,

    generate_interview_questions,

    generate_resume_summary
)

# ---------------------------------------------------
# Streamlit Configuration
# ---------------------------------------------------

st.set_page_config(

    page_title="AI Resume Analyzer",

    page_icon="📄",

    layout="wide"
)

# ---------------------------------------------------
# Custom CSS
# ---------------------------------------------------

st.markdown(
    """

    <style>

    .main {
        background-color: #0E1117;
        color: white;
    }

    .stButton>button {

        background-color: #4CAF50;

        color: white;

        border-radius: 10px;

        height: 3em;

        width: 100%;
    }

    .skill-box {

        background-color: #1E1E1E;

        padding: 10px;

        border-radius: 8px;

        margin: 5px;

        display: inline-block;
    }

    </style>

    """,

    unsafe_allow_html=True
)

# ---------------------------------------------------
# Title
# ---------------------------------------------------

st.title("📄 Enterprise AI Resume Analyzer")

st.write(
    """
    Upload your resume and compare it
    with the job description using
    AI-powered ATS analysis.
    """
)

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

st.sidebar.header("⚙ Settings")

show_resume_text = st.sidebar.checkbox(
    "Show Resume Text"
)

show_interview_questions = st.sidebar.checkbox(
    "Generate Interview Questions"
)

# ---------------------------------------------------
# File Upload
# ---------------------------------------------------

uploaded_file = st.file_uploader(

    "Upload Resume",

    type=["pdf", "docx"]
)

# ---------------------------------------------------
# Job Description Input
# ---------------------------------------------------

job_description = st.text_area(

    "Paste Job Description",

    height=250,

    placeholder="""
Paste complete job description here...
"""
)

# ---------------------------------------------------
# Analyze Button
# ---------------------------------------------------

if st.button("🚀 Analyze Resume"):

    if uploaded_file is not None and job_description != "":

        # ---------------------------------------------------
        # Save Uploaded File Temporarily
        # ---------------------------------------------------

        with tempfile.NamedTemporaryFile(

            delete=False,

            suffix=os.path.splitext(
                uploaded_file.name
            )[1]

        ) as tmp_file:

            tmp_file.write(
                uploaded_file.read()
            )

            temp_path = tmp_file.name

        # ---------------------------------------------------
        # Extract Resume Text
        # ---------------------------------------------------

        resume_text = extract_text(
            temp_path
        )

        # ---------------------------------------------------
        # Extract Skills
        # ---------------------------------------------------

        resume_skills = extract_skills(
            resume_text
        )

        jd_skills = extract_skills(
            job_description
        )

        # ---------------------------------------------------
        # ATS Score
        # ---------------------------------------------------

        ats_score = semantic_match_score(

            resume_text,

            job_description
        )

        # ---------------------------------------------------
        # Missing Skills
        # ---------------------------------------------------

        missing_skills = recommend_skills(

            resume_skills,

            jd_skills
        )

        # ---------------------------------------------------
        # Feedback
        # ---------------------------------------------------

        feedback = generate_feedback(

            ats_score,

            missing_skills
        )

        # ---------------------------------------------------
        # Resume Strength
        # ---------------------------------------------------

        strength = resume_strength(
            ats_score
        )

        # ---------------------------------------------------
        # Summary
        # ---------------------------------------------------

        summary = generate_resume_summary(

            resume_skills,

            ats_score
        )

        # ---------------------------------------------------
        # Layout Columns
        # ---------------------------------------------------

        col1, col2 = st.columns(2)

        # ===================================================
        # LEFT COLUMN
        # ===================================================

        with col1:

            st.subheader("📊 ATS Match Score")

            st.progress(
                min(int(ats_score), 100)
            )

            st.success(
                f"{ats_score}% Match"
            )

            st.subheader("📈 Resume Strength")

            if strength == "Strong Resume":

                st.success(strength)

            elif strength == "Good Resume":

                st.info(strength)

            elif strength == "Average Resume":

                st.warning(strength)

            else:

                st.error(strength)

            # ---------------------------------------------------
            # Skills
            # ---------------------------------------------------

            st.subheader("🛠 Extracted Skills")

            if len(resume_skills) > 0:

                for skill in resume_skills:

                    st.markdown(

                        f"""
                        <div class='skill-box'>
                        {skill}
                        </div>
                        """,

                        unsafe_allow_html=True
                    )

            else:

                st.warning(
                    "No skills detected."
                )

            # ---------------------------------------------------
            # Missing Skills
            # ---------------------------------------------------

            st.subheader("❌ Missing Skills")

            if len(missing_skills) > 0:

                for skill in missing_skills:

                    st.error(skill)

            else:

                st.success(
                    "No major skills missing."
                )

        # ===================================================
        # RIGHT COLUMN
        # ===================================================

        with col2:

            # ---------------------------------------------------
            # Feedback
            # ---------------------------------------------------

            st.subheader("💡 ATS Feedback")

            for item in feedback:

                st.write("✔", item)

            # ---------------------------------------------------
            # Resume Summary
            # ---------------------------------------------------

            st.subheader("📝 Resume Summary")

            st.info(summary)

            # ---------------------------------------------------
            # Interview Questions
            # ---------------------------------------------------

            if show_interview_questions:

                st.subheader(
                    "🎯 Interview Questions"
                )

                questions = generate_interview_questions(
                    missing_skills
                )

                if len(questions) > 0:

                    for q in questions:

                        st.write("•", q)

                else:

                    st.success(
                        "No interview questions generated."
                    )

        # ---------------------------------------------------
        # Resume Text
        # ---------------------------------------------------

        if show_resume_text:

            st.subheader("📄 Extracted Resume Text")

            st.text_area(

                "Resume Content",

                resume_text,

                height=400
            )

        # ---------------------------------------------------
        # Cleanup
        # ---------------------------------------------------

        os.remove(temp_path)

    else:

        st.error(
            "Please upload resume and paste job description."
        )

# ---------------------------------------------------
# Footer
# ---------------------------------------------------

st.markdown("---")

# FOOTER

st.markdown("""
<!-- Load Font Awesome Icon Library -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

<div class="footer" style="text-align: center; margin-top: 2rem; font-family: sans-serif;">
    Developed ❤️ by <span style="color: #38bdf8; font-weight: 600;">Shibam</span> | 
    <a href="https://github.com/myselfshibam" 
       target="_blank" 
       style="color: #38bdf8; text-decoration: none; font-weight: 600; margin-left: 5px;">
        <i class="fa-brands fa-github" style="margin-right: 5px;"></i>
    </a>  
    <a href="https://linkedin.com/in/shibammitra89" 
       target="_blank" 
       style="color: #38bdf8; text-decoration: none; font-weight: 600;">
        <i class="fa-brands fa-linkedin"></i>
    </a>
</div>
""", unsafe_allow_html=True)