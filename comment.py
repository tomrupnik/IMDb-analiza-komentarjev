from langdetect import detect
import spacy
import datetime

class Comment():

    def __init__(self, user, comment, date, mark, adjectives, polarity):
        self._user = user
        self._comment = comment
        self._date = date
        self._mark = mark
        self._adjectives = adjectives
        self._polarity = polarity

    @property
    def user(self):
        return self._user
    
    @property 
    def comment(self):
        return self._comment
    
    @property
    def date(self):
        return self._date
    
    @property
    def mark(self):
        return self._mark

    @user.setter
    def user(self, value):
        self._user = value

    @comment.setter
    def comment(self, value):
        self._comment = value
    
    @date.setter
    def date(self, value):
        self._date = value

    @mark.setter
    def mark(self, value):
        self._mark = value

    @staticmethod
    def get_adjectives(text):
        """
        Returns a list of adjectives in a given string.
        """
        adjectives = []
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(text)
        for token in doc:
            if token.is_alpha: 
                if token.pos_ == 'ADJ':
                    adjectives.append(token.lemma_)
        return adjectives

    @staticmethod
    def is_english(text):
        """
        Checks if a given string is written in English.
        """
        try:
            is_en = detect(text) == 'en'
        except Exception:
            is_en = None
        return is_en

    def to_date(self):
        months = {"January": 1, "February": 2, "March": 3, "April": 4, "May" : 5, "June": 6, "July": 7, "August": 8,
                "September": 9, "October": 10, "November": 11, "December": 12}
        d, m ,y = self._date.split()
        day = int(d)
        month = months[m]
        year = int(y)
        date = datetime.date(year, month, day)
        return date

    


        

    



    


        

    

