# Enterprise-AI-Resume-Analyzer-ATS-Screening-System

An AI-powered Resume Analyzer and ATS Screening System built using Machine Learning and Natural Language Processing (NLP). The application analyzes resumes, compares them with job descriptions, and generates ATS compatibility scores along with personalized feedback and skill recommendations.

---

## 🚀 Features

- 📑 Resume Parsing (PDF & DOCX)
- 🤖 AI-powered ATS Score Prediction
- 🔍 Semantic Resume-Job Matching
- 🛠 Skill Extraction and Missing Skill Detection
- 💡 Resume Feedback Generation
- 📈 Resume Strength Analysis
- 🎯 Interview Question Recommendation
- 🖥 Interactive Streamlit Dashboard
- ⚡ Real-Time Resume Analysis

---

## 🛠 Tech Stack

- **Python**
- **Streamlit**
- **Scikit-learn**
- **Sentence Transformers**
- **Natural Language Processing (NLP)**
- **Pandas**
- **NumPy**
- **Cosine Similarity**

---

## 📂 Project Structure

```
resume-analyzer/
│
├── app/
│   ├── backend/
│   │   ├── parser.py
│   │   ├── recommendation.py
│   │   ├── skill_extractor.py
│   │
│   ├── frontend/
│   │   └── stream_app.py
│
├── data/
├── models/
├── experimentation.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/resume-analyzer.git
cd resume-analyzer
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

#### Mac/Linux

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app/frontend/stream_app.py
```

Open:

```
http://localhost:8501
```

---

## 📊 Functionalities

### ✅ ATS Score Prediction

Compares resumes with job descriptions using semantic similarity techniques.

### ✅ Resume Parsing

Extracts text from PDF and DOCX resumes automatically.

### ✅ Skill Extraction

Identifies technical skills present in resumes.

### ✅ Missing Skill Recommendation

Suggests skills missing from the resume based on job requirements.

### ✅ Resume Feedback

Provides AI-driven suggestions to improve resume quality.

### ✅ Interview Preparation

Generates interview questions based on identified skills.

---

## 📸 Demo

Upload Resume ➜ Paste Job Description ➜ Check ATS Score ➜ Get Feedback & Recommendations

---

## 🎯 Future Enhancements

- Multi-Resume Ranking System
- Recruiter Dashboard
- Resume Summarization with LLMs
- PDF Report Generation
- Candidate Recommendation Engine
- MLOps Pipeline Integration
- Docker Deployment
- FastAPI Backend

---

## 📚 Learning Outcomes

- Machine Learning
- Natural Language Processing
- Semantic Similarity
- Streamlit Application Development
- Feature Engineering
- Recommendation Systems
- End-to-End AI Project Development

---

## 👨‍💻 Author

**Shibam Mitra**

- 📧 Email: **mitrashibam89@gmail.com**
- 💼 LinkedIn: **https://www.linkedin.com/in/shibammitra89**
- 🔗 GitHub: **https://github.com/myselfshibam**

---

⭐ If you found this project useful, please consider giving it a star!
