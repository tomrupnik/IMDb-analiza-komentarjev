from operator import index
import pandas as pd
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("spacytextblob")

def sent_analyse(text):
    """
    Calculates polarity for argument text.
    """
    doc = nlp(text)
    return doc._.blob.polarity

def get_polarity(data):
    """
    Calculates polarity for all lists of adjectives in a given pd.DataFrame
    """
    grades = []
    for _,comment in data.iterrows():
        adjectives = " ".join(eval(comment["adjectives"]))
        grade = sent_analyse(adjectives)
        grades.append(grade)
    return grades


def csv_add_polarity(data, all_grades, file):
    """
    Adds polarity column to csv file.
    """
    data["polarity"] = all_grades
    data.to_csv("data/" + file + ".csv", sep = ";", index = False)
