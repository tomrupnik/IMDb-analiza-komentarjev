import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


read_file = pd.read_csv("data/movies.csv", sep = ';')
marks = []
polaritys = []
for _, row in read_file.iterrows():
    file = row["file_name"]
    data = pd.read_csv("data/" + file + ".csv", sep = ';')
    for _, row in data.iterrows():
        polarity = row["polarity"]
        mark = row["mark"]
        marks.append(mark)
        polaritys.append(polarity) 

# Regression line
coef = np.polyfit(marks, polaritys, 1)
line = np.poly1d(coef)
x_axis = [0.8] + marks + [10.2]

graph = plt.figure(figsize = [10, 5])
plt.plot(marks, polaritys, "b.", x_axis, line(x_axis), "-r")
plt.title("Povezava polarnosti in ocen predstavljena z \n regresijsko premico")
plt.xlabel("Ocene filmov")
plt.ylabel("Polarnost")
graph.savefig("image/mark_polarity_graph.pdf")
