from adjectives import *
from grade_new import *
from graph import *
from movie import *

read_file = pd.read_csv("data/movies.csv", sep = ';')
for _, row in read_file.iterrows():
     file_name = row["file_name"]
     data = pd.read_csv("data/" + file_name + ".csv", sep = ';')
     movie = Movie(file_name)
     polaritys = data["polarity"].tolist()
     intervals = frequency(polaritys)
     title = row["movie_title"].capitalize()
     draw_bar_plot(intervals, f"{file_name}_bar_plot", title)

     top_adje = top_ten_adjectives(movie.get_common_words())
     plot_top10(top_adje, f"{file_name}_top_plot", title)

     # PIE CHART
     all_marks = data["mark"].tolist()
     plot_by_grade(all_marks, f"{file_name}_pie_chart", title)
          



