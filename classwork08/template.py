def task1():
    a = int(input())
    b = int(input())
    print(a ** 2 - b ** 2)

def task2():
    s = str(input())
    count = 0
    for letter in s:
        if 47 < ord(letter) < 58:
            count += 1
    print(count)

def task3():
    a = list(map(str, input().split()))
    # print(a)
    count = 0
    for word in a:
        if len(word) >= 3:
            if (word[0] == 'a') and (word[1] == 'b') and (word[-1] == 'a') and (word[-2] == 'b'):
                count += 1
    print(count)

def task4(generator):
    c = list(filter(lambda x: x.find('sus') > -1, generator))
    print(*c)

def task5(list_of_smth):
    b = list_of_smth[4:-1:3]
    print(b[::-1])

def task6(list1, list2, list3, list4):
    A = set(list1)
    B = set(list2)
    C = set(list3)
    D = set(list4)

    print((A & D) | (C & B))

def task7():
    import numpy as np
    np.random.seed(2)
    arr = np.random.randint(65, size=64)
    # print(array)

    matrix = arr.reshape(8, 8)
    print(matrix)
    matrix = np.delete(matrix, (7), axis=0)
    matrix = np.delete(matrix, (0), axis=1)
    print(np.linalg.det(matrix))


def task8(f, min_x, max_x, N, min_y, max_y):
    import matplotlib
    from matplotlib import pyplot as plt
    import numpy as np
    x = np.linspace(min_x, max_x, N)
    y = f(x)
    plt.yscale('log')
    plt.grid(True)
    plt.plot(x, y, color='red')
    plt.ylim((min_y, max_y))

    plt.savefig('function.jpeg')
    plt.show()

def task9(data, x_array, y_array, threshold):
    # TODO: ...

def task10(list_of_smth, n):
    a = list_of_smth
    b = []
    for i in range(len(a)):
        b.append(0)
        if len(a) - 1 <= n:
            for j in range(i, i + n):
                b[i] = b[i] + a[j] ** 2
            b[i] = (b[i] / n) ** 0.5
        else:
            for j in range(i, len(a)):
                b[i] = b[i] + a[j] ** 2
            b[i] = (b[i] / (len(a) - i)) ** 0.5
    print(b)

def task11(filename="infile.csv"):
    # TODO: ...

def task12(filename="video-games.csv"):
    import pandas as pd
    f = pd.read_csv("video-games.csv")
    n_games = len(f['title'].value_counts())

    by_years = f.groupby(["year"]).agg({"title": "count"})

    mean_price = f.groupby(["publisher"]).agg({"price": "mean"}).loc['EA'][0]

    # m = f.groupby(["age_raiting"]).agg({"price": "max"})
    # k = f["price"] == m
    # age_max_price = age_max_price['title']

    # mean_raiting_1_2 = f.groupby(["max_players"]).agg({"review_raiting": "mean"}).loc['1'][0]

    min_max_price = f.groupby(["age_raiting"]).agg({"price": "max"})
    min_max_price['min_price'] = f.groupby(["age_raiting"]).agg({"price": "min"})
    min_max_price['sales_metric'] = f.groupby(["age_raiting"]).agg({"sales_metric": "mean"})

    n_games_by_age = f.groupby(["review_raiting"]).agg({"title": "count"})

    # max_raiting_by_years = f.groupby(["year"]).agg({"review_raiting": "count"})

    print(f)
    print(n_games)
    print(by_years)
    print(mean_price)
    print(min_max_price)
    print(n_games_by_age)
