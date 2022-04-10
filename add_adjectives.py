from comment import *
import pandas as pd

read_file = pd.read_csv("data/movies.csv", sep = ';')
print(read_file)
for _, row in read_file.iterrows():
    file = row["file_name"]
    data = pd.read_csv("data/" + file + ".csv", sep = ';')
    all_users = []

    for _, row in data.iterrows():
        adj = Comment.get_adjectives(row["comment"])
        all_users.append(adj)
    
    data["adjectives"] = all_users
    data.to_csv("data/" + file + ".csv", sep = ';', index = False)

