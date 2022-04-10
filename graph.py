import matplotlib.pyplot as plt

def frequency(grades):
    counter = [0]*10
    for grade in grades:
        if grade < -0.8:
            counter[0] += 1
        elif grade < -0.6:
            counter[1] += 1
        elif grade < -0.4:
            counter[2] += 1
        elif grade < -0.2:
            counter[3] += 1
        elif grade < -0.0:
            counter[4] += 1
        elif grade < 0.2:
            counter[5] += 1
        elif grade < 0.4:
            counter[6] += 1
        elif grade < 0.6:
            counter[7] += 1
        elif grade < 0.8:
            counter[8] += 1
        else:
            counter[9] += 1
    return counter

# =============================graf poz/neg komentarjev===========================
def draw_bar_plot(interval, file_name, title):
    """
    Draws a graph of number of comment in relation to polarity
    """
    x_axis = ["-0.8", "-0.6", "-0.4", "-0.2", "0", "0.2", "0.4", "0.6", "0.8", "1"]

    graph = plt.figure(figsize = [8, 5])
    plt.bar(x_axis,interval)
    for i in range(len(x_axis)):
        plt.text(i,interval[i],interval[i],ha="center")
    plt.title(f"Razporeditev pozitivnosti/negativnosti komentarjev \n {title}")
    plt.xlabel("Zgornje meje intervalov s korakom 0.2")
    graph.savefig(f"image/{file_name}.pdf")

# ============================graf top10 pridevnikov=============================
def plot_top10(data, file_name, title):
    """
    Draws ten most common adjectives for a given movie.
    """
    x = []
    y = []
    for k,v in data.items():
        x.append(k.upper())
        y.append(v)
        
    graph2 = plt.figure(figsize = [10, 5])
    plt.bar(x,y)
    for i in range(len(x)):
        plt.text(i, y[i], y[i], ha = "center")
    plt.title(f"10 najbolj pogostih pridevnikov  \n {title}")
    graph2.savefig(f"image/{file_name}.pdf")

def plot_by_grade(ocene, file_name, title):
    """
    Draws a graph of number of comments in relation to the mark.
    """
    labels = ["1","2","3","4","5","6","7","8","9","10"]
    y = [0]*10
    for i in range(10):
        y[i] = ocene.count(i+1)
    graph3 = plt.figure(figsize = [10, 5])
    plt.pie(y, labels = labels, shadow = True, startangle = 90, pctdistance = 1)
    plt.axis('equal')
    plt.title(f'Razporeditev ocen komentarjev  \n {title}', pad = 15)
    graph3.savefig(f"image/{file_name}.pdf")
    