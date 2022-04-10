import pandas as pd
from grade_new import *
read_file = pd.read_csv("data/movies.csv", sep = ';')
for _, row in read_file.iterrows():
    file_name = row["file_name"]
    read = pd.read_csv("data/" + file_name + ".csv", sep = ';')
    polaritys = get_polarity(read)
    csv_add_polarity(read, polaritys, file_name)
