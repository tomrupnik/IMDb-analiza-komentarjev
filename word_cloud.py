import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from adjectives import top_ten_adjectives #, get_all_adjectives
from movie import *

read_file = pd.read_csv("data/movies.csv", sep = ';')
for _, row in read_file.iterrows():
    title = row["movie_title"].capitalize()
    file = row["file_name"]
    data = pd.read_csv("data/" + file + ".csv", sep = ';')
    all_adjectives = Movie(file).get_common_words()
    top_30 = top_ten_adjectives(all_adjectives, 30)
    wordcloud = WordCloud(width = 600,height=400).generate(" ".join(top_30))
    graph = plt.figure(figsize = [10, 5])
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.title(f"30 najbolj pogostih opisnih pridevnikov  \n {title}")
    graph.savefig(f"image/{file}_wordcloud.pdf")


