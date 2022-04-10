import requests
import re
import csv
from bs4 import BeautifulSoup

OMDB_API_KEY = 'cd9ba7d7'

def get_movie_genre(name):
    name = name.replace(' ', '+')
    url_api = "http://www.omdbapi.com/?apikey={:s}&t={:s}".format(OMDB_API_KEY, name)
    req = requests.get(url_api)
    json = req.json()
    try:
        genre = json['Genre']
    except KeyError:
        genre = ''
    return genre

url = "https://www.imdb.com/chart/top/" # URl Top Movies
headers = {"Accept-Language": "en-US,en;q=0.5"}
req = requests.get(url, headers=headers)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
content = soup.find_all(class_ = 'titleColumn')
header = ['id', 'movie_title', 'movie_code', 'file_name', 'reviews_link', 'genre']

i = 1
with open('data/movies.csv', 'w', encoding = 'UTF-8', newline = '') as file:
    writer = csv.writer(file, delimiter = ';')
    writer.writerow(header)
    for movie in content:
        print(i)
        regex_movie_code = r'<a href="/title/(.*)/" title=".*">.*</a>'
        regex_movie_title = r'<a href="/title/.*/" title=".*">(.*)</a>'
        regex_replace = r'[^\w]+'
        movie_code = re.findall(regex_movie_code, str(movie))
        link = 'https://www.imdb.com/title/' + movie_code[0] + '/reviews?ref_=tt_urv'
        movie_title = re.findall(regex_movie_title, str(movie))
        file_name = re.sub(regex_replace, '_', str(movie_title[0])).lower()
        writer.writerow([i, movie_title[0], movie_code[0], file_name, link, get_movie_genre(movie_title[0])])
        if i == 20: # Only 20 top movies
            break
        i += 1

