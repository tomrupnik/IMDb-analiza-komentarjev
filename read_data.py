import requests
import re
from bs4 import BeautifulSoup
import csv
from comment import *
from cleantext import clean

def read_html(url):
    response = requests.get(url)
    content = response.text
    return content

def get_data_key(html):
    regex_data_key = r'data-key=\"([^\"]*)'
    data_key = re.findall(regex_data_key, html)
    if data_key == []:
        return None
    return data_key[0]

def get_content(html):
    """
    The function returns the content of lister-item-content class.
    """
    soup = BeautifulSoup(html, "html.parser")
    content = soup.find_all(class_="lister-item-content")
    return content

def write_data(file_name, content):
    """
    The function writes the data into a CSV file.
    """
    i = 1
    with open("data/" + file_name + ".csv", 'w', newline='') as f:
        header = ["id", "user", "comment", "date", "mark"]
        file_writer = csv.writer(f, delimiter = ';')
        file_writer.writerow(header)
        for review in list(content):
            regex_mark = r'<span>(.*)</span><span class="point-scale">/10</span>'
            regex_date = r'<span class="review-date">(.*)</span>'
            regex_user = r'<a href="\/user\/.*\/\">([^>]*)<\/a>' 
            regex_comment = r'<div class="text show-more__control[ clickable]*">(.*\s?.*)</div>'
            mark = re.findall(regex_mark, str(review))
            if mark == []:
                continue
            else:
                mark = mark[0]
            date = re.findall(regex_date, str(review))[0]
            user = re.findall(regex_user, str(review))[0]
            comment = re.findall(regex_comment, str(review))
            if comment == []:
                comment = re.findall(regex_comment, str(review),re.DOTALL)
            regex_replace = r'</div>(.*\s*)*'
            comment = re.sub(regex_replace,'',comment[0])
            comment = re.sub(r'<br/>', ' ', comment)
            comment = clean(comment, no_emoji = True, no_line_breaks = True)
            id = i - 1
            if not Comment.is_english(comment):
                continue
            file_writer.writerow([id, user, comment , date, mark])
            i += 1

def write_to_file(url, file_name, movie_code):
    content = []
    html = read_html(url)
    data_key = get_data_key(html)
    while data_key != None:
        content += get_content(html)
        url = "https://www.imdb.com/title/" + movie_code + "/reviews/_ajax?ref_=undefined&paginationKey=" + data_key
        html = read_html(url)
        data_key = get_data_key(html)
    write_data(file_name, content)