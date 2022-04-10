import pandas as pd

class Movie():
    def __init__(self, movie):
        self._movie = movie

    def get_all_users(self):
        """
        Returns a set of all users that have commented on a movie.
        """
        read_file = pd.read_csv("data/" + self._movie + ".csv")
        users = set(read_file["user"].tolist())
        return users

    def get_users(self):
        """
        Returns a set of users that have marked the film with mark 10.
        """
        read_file = pd.read_csv("data/" + self._movie + ".csv", sep = ';')
        return set(read_file.loc[read_file["mark"] == 10]["user"].tolist())

    def get_common_words(self):
        """
        Retruns a dictionary of most common addjectives sorted by their occurence in user reviews.
        """
        words = dict()
        read_file = pd.read_csv("data/" + self._movie + ".csv", delimiter = ';')
        for _, row in read_file.iterrows():
            adjectives = row["adjectives"]
            ls_adjectives = eval(adjectives)
            for adjective in ls_adjectives:
                if not adjective in words.keys():
                    words[adjective] = 1
                else:
                    words[adjective] += 1
        return dict(sorted(words.items(), key = lambda x: -x[1]))

    def get_polaritys(self):
        """Retruns all the polarity for every comment in form of a list."""
        polaritys = list()
        read_file = pd.read_csv("data/" + self._movie + ".csv", delimiter = ';')
        for _, row in read_file.iterrows():
            polarity = row["polarity"]
            polaritys.append(polarity)
        return polaritys

    def get_avg_polarity(self):
        """Returns the average polarity of comments in a movie."""
        read = pd.read_csv("data/" + self._movie + ".csv", delimiter = ';')
        polarity_sum = 0
        number_of_rows = 0
        for _, row in read.iterrows():
            polarity = row["polarity"]
            polarity_sum += polarity
            number_of_rows += 1
        return polarity_sum/number_of_rows




