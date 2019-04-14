import pandas as pd
import spacy
import csv
from pdftotextconvertor import convert_PDFtoText


resume_string = convert_PDFtoText("../Coding-Assignment/resume-parser/myresume.pdf")
resume_string = resume_string.decode().replace(',', ' ').lower()


nlp = spacy.load('en_core_web_sm')
doc = nlp(resume_string)
noun_chunks = doc.noun_chunks


def extract_skills(resume_text):
    nlp_text = nlp(resume_text)

    # removing stop words and doing word tokenization
    tokens = [token.text for token in nlp_text if not token.is_stop]
    print(tokens)

    data = pd.read_csv("../Coding-Assignment/resume-parser/technicalskills.csv") 
    
    # extract values
    skills = list(data.columns.values)
    print(skills)

    skillset = []

    
    for token in tokens:
        #print(token)
        if token in skills:
            skillset.append()
    
    # check for bi-grams and tri-grams (example: machine learning)
    for token in noun_chunks:
        #print(token)
        token = token.text.lower().strip()
        if token in skills:
            skillset.append(token)

    myskills = [i.capitalize() for i in set([i.lower() for i in skillset])]
    print(myskills)

    return myskills


extract_skills(resume_string)