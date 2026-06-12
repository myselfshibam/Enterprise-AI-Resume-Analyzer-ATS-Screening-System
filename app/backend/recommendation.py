# recommendation.py

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# -------------------------------------------------
# Load Pretrained BERT Model
# -------------------------------------------------

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# -------------------------------------------------
# ATS Semantic Match Score
# -------------------------------------------------

def semantic_match_score(
    resume_text,
    job_description
):
    """
    Calculate ATS similarity score
    using semantic embeddings
    """

    resume_embedding = model.encode(
        [resume_text]
    )

    jd_embedding = model.encode(
        [job_description]
    )

    similarity = cosine_similarity(
        resume_embedding,
        jd_embedding
    )

    score = round(
        similarity[0][0] * 100,
        2
    )

    return score


# -------------------------------------------------
# Skill Extraction
# -------------------------------------------------

def extract_skills(text):
    """
    Extract important skills
    """

    skills_database = [

        "python",
        "machine learning",
        "deep learning",
        "sql",
        "nlp",
        "tensorflow",
        "pytorch",
        "docker",
        "aws",
        "azure",
        "power bi",
        "tableau",
        "pandas",
        "numpy",
        "opencv",
        "flask",
        "fastapi",
        "streamlit",
        "mongodb",
        "postgresql",
        "scikit-learn",
        "keras",
        "linux",
        "git",
        "data analysis"
    ]

    text = text.lower()

    found_skills = []

    for skill in skills_database:

        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))


# -------------------------------------------------
# Missing Skills Recommendation
# -------------------------------------------------

def recommend_skills(
    resume_skills,
    jd_skills
):
    """
    Find missing skills
    """

    missing_skills = []

    resume_skills = [
        skill.lower()
        for skill in resume_skills
    ]

    for skill in jd_skills:

        if skill.lower() not in resume_skills:
            missing_skills.append(skill)

    return list(set(missing_skills))


# -------------------------------------------------
# ATS Feedback Generator
# -------------------------------------------------

def generate_feedback(
    ats_score,
    missing_skills
):
    """
    Generate smart resume feedback
    """

    feedback = []

    # ATS score feedback

    if ats_score >= 85:

        feedback.append(
            "Excellent ATS compatibility."
        )

        feedback.append(
            "Your resume is highly optimized."
        )

    elif ats_score >= 70:

        feedback.append(
            "Good ATS score."
        )

        feedback.append(
            "Improve project descriptions."
        )

    elif ats_score >= 50:

        feedback.append(
            "Resume needs optimization."
        )

        feedback.append(
            "Add more technical keywords."
        )

    else:

        feedback.append(
            "Low ATS score detected."
        )

        feedback.append(
            "Tailor your resume according to the job description."
        )

    # Missing skills feedback

    if len(missing_skills) > 0:

        feedback.append(
            f"Missing Skills: {', '.join(missing_skills)}"
        )

    else:

        feedback.append(
            "No major skills missing."
        )

    return feedback


# -------------------------------------------------
# Resume Strength Analyzer
# -------------------------------------------------

def resume_strength(ats_score):
    """
    Analyze resume quality
    """

    if ats_score >= 85:
        return "Strong Resume"

    elif ats_score >= 70:
        return "Good Resume"

    elif ats_score >= 50:
        return "Average Resume"

    else:
        return "Weak Resume"


# -------------------------------------------------
# Candidate Ranking System
# -------------------------------------------------

def rank_candidates(candidate_data):
    """
    Rank multiple candidates
    """

    ranked = sorted(
        candidate_data,
        key=lambda x: x["ATS Score"],
        reverse=True
    )

    return ranked


# -------------------------------------------------
# Keyword Density Checker
# -------------------------------------------------

def keyword_density(
    resume_text,
    keywords
):
    """
    Check keyword frequency
    """

    resume_text = resume_text.lower()

    total_words = len(
        resume_text.split()
    )

    density = {}

    for keyword in keywords:

        count = resume_text.count(
            keyword.lower()
        )

        percentage = round(
            (count / total_words) * 100,
            2
        )

        density[keyword] = {

            "count": count,
            "percentage": percentage
        }

    return density


# -------------------------------------------------
# Interview Question Generator
# -------------------------------------------------

def generate_interview_questions(
    missing_skills
):
    """
    Generate interview questions
    """

    question_bank = {

        "python":
        "Explain Python decorators.",

        "machine learning":
        "What is overfitting in ML?",

        "deep learning":
        "Explain backpropagation.",

        "sql":
        "Difference between JOIN and UNION?",

        "docker":
        "What is Docker containerization?",

        "aws":
        "Explain AWS EC2 service.",

        "nlp":
        "What is tokenization in NLP?",

        "tensorflow":
        "What are tensors?",

        "pytorch":
        "Difference between TensorFlow and PyTorch?"
    }

    questions = []

    for skill in missing_skills:

        skill = skill.lower()

        if skill in question_bank:

            questions.append(
                question_bank[skill]
            )

    return questions


# -------------------------------------------------
# Resume Summary Generator
# -------------------------------------------------

def generate_resume_summary(
    resume_skills,
    ats_score
):
    """
    Generate short resume summary
    """

    summary = f"""

Candidate has expertise in:
{', '.join(resume_skills)}.

ATS Compatibility Score:
{ats_score}%.

"""

    return summary


# -------------------------------------------------
# Example Testing
# -------------------------------------------------

if __name__ == "__main__":

    resume_text = """

    Python developer with experience
    in Machine Learning, NLP,
    Docker and AWS.

    """

    job_description = """

    Looking for ML Engineer with
    Python, Docker, AWS and NLP skills.

    """

    # ATS Score

    ats_score = semantic_match_score(
        resume_text,
        job_description
    )

    print("\nATS Score:")
    print(ats_score)

    # Extract Skills

    resume_skills = extract_skills(
        resume_text
    )

    jd_skills = extract_skills(
        job_description
    )

    print("\nResume Skills:")
    print(resume_skills)

    # Missing Skills

    missing = recommend_skills(
        resume_skills,
        jd_skills
    )

    print("\nMissing Skills:")
    print(missing)

    # Feedback

    feedback = generate_feedback(
        ats_score,
        missing
    )

    print("\nFeedback:")

    for item in feedback:
        print("-", item)

    # Resume Strength

    strength = resume_strength(
        ats_score
    )

    print("\nResume Strength:")
    print(strength)

    # Interview Questions

    questions = generate_interview_questions(
        missing
    )

    print("\nInterview Questions:")

    for q in questions:
        print("-", q)

    # Summary

    summary = generate_resume_summary(
        resume_skills,
        ats_score
    )

    print("\nResume Summary:")
    print(summary)