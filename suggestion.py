from movie import *
import pandas as pd
import time
import networkx as nx
import matplotlib.pyplot as plt

read_file = pd.read_csv("data/movies.csv", sep = ';')
movie_file = read_file["file_name"].tolist()
movie_title = read_file["movie_title"].tolist()
movies = dict(zip(movie_file, movie_title))
suggestions = {key:[] for key in movie_title}
for movie in movie_file:
    users = Movie(movie).get_users()
    for suggest in movie_file:
        if movie == suggest:
            continue
        users_suggest = Movie(suggest).get_users()
        if len(users.intersection(users_suggest)) >= 70:
            suggestions[movies[movie]] += [movies[suggest]]


fig = plt.figure(figsize = (16, 9))
graph = nx.Graph(suggestions)
degree = nx.degree(graph)
nx.draw_kamada_kawai(graph, with_labels = True, node_color = "#D3212D", 
                    node_size = [60 * value[1] if value[1] != 0 else 40 for value in degree],
                    font_size = 10, font_weight = "bold")
plt.savefig("image/network.png", dpi = 300, bbox_inches = "tight")
plt.show()


