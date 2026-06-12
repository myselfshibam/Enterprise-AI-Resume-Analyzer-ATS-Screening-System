import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS = [
    "python",
    "machine learning",
    "deep learning",
    "sql",
    "tensorflow",
    "pytorch",
    "docker",
    "aws",
    "nlp",
    "power bi"
]

def extract_skills(text):

    doc = nlp(text.lower())

    found_skills = []

    for token in doc:
        if token.text in SKILLS:
            found_skills.append(token.text)

    return list(set(found_skills))