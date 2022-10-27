from random import Random


def task1():
    a = int(input())
    b = int(input())
    print((a+b)**2)

def task2():
    s = input()
    sum = 0
    A = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for x in s:
        if x in A:
            sum+=1
    print(sum)

def task3():
    sum_1 = 0
    f = input()
    f = f.split()
    for x in f:
        if "sus" in x:
            sum_1+=1
    print(sum_1)
    

def task4(generator):
    a = generator
    a = list(filter(lambda x: "sus" not in x, a))
    

def task5(list_of_smth):
    print(*list_of_smth[-2:4:-3])

def task6(list1, list2, list3, list4):
    q = (list1 | list2)
    w = (list3 | list4)
    print(q&w)

def task7():
    import numpy as np
    np.random.seed(6)
    a = np.random.randint(0, 49, size=49)
    matrix = a.reshape(7,7)
    print(matrix[:6:,:6:])

def task8(f, min_x, max_x, N, min_y, max_y):
    import numpy as np
    import matplotlib.pyplot as plt
    x = np.linspace(min_x,max_x,N)
    y = f(x)
    plt.yscale("log")
    plt.ylabel("log (y)")
    plt.xlabel("x")
    plt.grid(which='major',
        color = 'k', 
        linewidth = 2)
    plt.plot(x,y, color = "green", linestyle = ":")
    plt.savefig('function.png')
    

def task9(data, x_array, y_array):
    # TODO: ...

def task10(list_of_smth):
    # TODO: ...

def task11(filename="infile.csv"):
    # TODO: ...

def task12(filename="video-games.csv"):
    import pandas as pd
    import numpy as np
    g = pd.read_csv(filename)
    g["Amount"] = g["Unnamed: 0"]
    g["max_price"]=g["price"]
    g_0 = g.groupby(g["year"]).agg({"Amount":"count"}).reset_index()
    g_1 = g.groupby(g["publisher"]).agg({"price":"mean"}).loc["EA"]
    g_2 = g.groupby(g["age_raiting"]).agg({"price":"max"}).reset_index()
    g_3 = g.groupby((g["max_players"]==1) | (g["max_players"]==2)).agg({"review_raiting":"mean"}).mean()[0]
    g_4 = g.groupby(g["review_raiting"]).agg({"Amount":"count"}).reset_index()
    g_5 = g.groupby(g["age_raiting"]).agg({"max_price":"max"}).sort_values(by= "max_price", ascending = False).reset_index()
    d = {"n_games" : g.shape[0], "by_years" : g_0, "mean_price" : g_1, "age_max_price" : g_2, "mean_raiting_1_2" : g_3, "n_games_by_age" : g_4 ,"min_max_price" : g_5}
