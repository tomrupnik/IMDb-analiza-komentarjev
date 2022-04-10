import pandas as pd
from comment import *

def top_ten_adjectives(dic, n = 10):
    """
    Returns a dictionary with n most common words as keys and occurence as it's value.
    """   
    top_10 = dict()
    i = 1
    for adj in sorted(dic, key=dic.get, reverse=True):
        top_10[adj] = dic[adj]
        if i >= n:
            break
        i+= 1
    return top_10

def numbers_user(data, dic):
    numbers = []
    for _, comment in data.iterrows():
        adjectives = comment["adjectives"]
        num = 0
        for adj in dic:
            num += adjectives.count(adj)
        numbers.append(num)
    return numbers
            




