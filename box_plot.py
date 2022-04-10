import pandas as pd
from movie import * 
import matplotlib.pyplot as plt
read_file = pd.read_csv("data/movies.csv", sep = ';')
i = 1
y = 1
polaritys = []
labels = []
for _, row in read_file.iterrows():
    file_name = row["file_name"]
    polarity = Movie(file_name).get_polaritys()
    polaritys += [polarity]
    title = row["movie_title"]
    if len(list(title.split())) >= 9:
        title = ' '.join(list(title.split())[0:5] +["\n"] + list(title.split())[5:])
    labels += [title]
    if i % 5 == 0:
        fig, ax = plt.subplots(figsize = (16, 9))
        ax.set_title("Polarity Box Plot " + str(y))
        ax.boxplot(polaritys, showfliers = False)
        ax.set_xticks([1, 2, 3, 4, 5])
        ax.set_xticklabels(labels)
        ax.grid()
        fig.savefig("image/" + str(y) + "_box_plot.pdf")
        y += 1
        polaritys = []
        labels = []
    i += 1

