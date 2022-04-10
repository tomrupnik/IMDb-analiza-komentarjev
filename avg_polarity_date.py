import pandas as pd
from comment import *
import matplotlib.pyplot as plt
from datetime import timedelta

read_file = pd.read_csv("data/movies.csv", sep = ';')
for _, row in read_file.iterrows():
    movie_title = row["movie_title"]
    file = row["file_name"]
    read = pd.read_csv("data/" + file + ".csv", sep = ';')
    polarity_date = []
    for _, row in read.iterrows():
        user = row["user"]
        comment = row["comment"]
        date = row["date"]
        mark = row["mark"]
        adjectives = row["adjectives"]
        polarity = row["polarity"]
        com = Comment(user, comment, date, mark, adjectives, polarity)
        polarity_date.append([polarity, com.to_date()])
    ordered_pol_date = sorted(polarity_date, key = lambda x: x[1])
    first = ordered_pol_date[0][1] # First date
    last = ordered_pol_date[-1][1] # Last date
    delta = last - first
    all_dates = [first] + [first + timedelta(days = i) for i in range(delta.days + 1)] + [last]
    all_dates = sorted(all_dates)

    avg_pol_by_date = [] #Average polarity by date
    for date in all_dates:
        sum_polarity = 0
        for index, element in enumerate(ordered_pol_date):
            polarity, dt = element
            if dt <= date:
                sum_polarity += polarity
            else:
                break
        avg_polarity = sum_polarity/(index + 1)
        avg_pol_by_date.append([avg_polarity, date])


    x = [x[1] for x in avg_pol_by_date] # Dates
    y = [x[0] for x in avg_pol_by_date] # Average polaritys

    fig, ax = plt.subplots(figsize = (10, 6))
    
    ax.plot(x, y)

    ax.set(xlabel="date", ylabel="average polarity of comments",
        title=f"Date - Average Polarity \n {movie_title}")
    ax.grid()
    fig.savefig("image/" + file + "_avg_pol.pdf")

    