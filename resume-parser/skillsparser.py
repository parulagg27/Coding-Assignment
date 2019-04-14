import pandas as pd
import numpy as np
import spacy
import csv
from pdftotextconvertor import convert_PDFtoText


resume_string = convert_PDFtoText("../Coding-Assignment/resume-parser/myresume.pdf")
#print(resume_string)
#print (type(resume_string))
resume_string = resume_string.decode().replace(',',' ')
#print(resume_string)
#resume_string = resume_string.lower()
#print(resume_string)

with open('../Coding-Assignment/resume-parser/technicalskills.csv', 'r') as f:
    reader = csv.reader(f)
    techskills = list(reader)
    #print(techskills)
    #print('\n')


with open('../Coding-Assignment/resume-parser/nontechskills.csv', 'r') as f:
    reader = csv.reader(f)
    nontechskills = list(reader)

s = set(techskills[0])
s1 = techskills

#print(s)
print('\n')
print(s1)

skillindex = []
skills = []

for token in resume_string.split(" "):
    #print (token)
    if token in s1:
        skills.append(token)

print(skills)

skills_list = list(set(skills))
#print(skills_list)

print("My Technical Skills are:")
print('\n')
np_a1 = np.array(techskills)

for i in range(len(skills)):
    item_index = np.where(np_a1==skills[i])
    skillindex.append(item_index[1][0])

nlen = len(skillindex)

for i in range(nlen):
    print(skills[i])
    #print(s2[0][skillindex[i]])
    print('\n')

s1 = set(nontechskills[0])
nontechskills = []
for word in resume_string.split(" "):
    if word in s1:
        nontechskills.append(word)
nontechskills = set(nontechskills)
print('\n')

print("Following are my Non Technical Skills")
list5 = list(nontechskills)
print('\n')
for i in range(len(list5)):
    print(list5[i])
