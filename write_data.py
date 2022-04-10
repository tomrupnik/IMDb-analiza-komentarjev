from read_data import *
import csv
with open("data/movies.csv", 'r') as f:
    file_reader = csv.DictReader(f, fieldnames = ["id", "movie_title", "movie_code", "file_name", "reviews_link", "genre"], delimiter = ';')
    next(file_reader)
    i = 1
    for row in file_reader:
        movie_code = row["movie_code"]
        title = row["file_name"]
        url = row["reviews_link"]
        write_to_file(url, title, movie_code)
        

