import pandas as pd
f = pd.read_csv("video-games.csv")
n_games = len(f['title'].value_counts())

by_years = f.groupby(["year"]).agg({"title": "count"})

mean_price = f.groupby(["publisher"]).agg({"price": "mean"}).loc['EA'][0]

#m = f.groupby(["age_raiting"]).agg({"price": "max"})
#k = f["price"] == m
#age_max_price = age_max_price['title']

#mean_raiting_1_2 = f.groupby(["max_players"]).agg({"review_raiting": "mean"}).loc['1'][0]

min_max_price = f.groupby(["age_raiting"]).agg({"price": "max"})
min_max_price['min_price'] = f.groupby(["age_raiting"]).agg({"price": "min"})
min_max_price['sales_metric'] = f.groupby(["age_raiting"]).agg({"sales_metric": "mean"})

n_games_by_age = f.groupby(["review_raiting"]).agg({"title": "count"})

#max_raiting_by_years = f.groupby(["year"]).agg({"review_raiting": "count"})

print(f)
print(n_games)
print(by_years)
print(mean_price)
print(min_max_price)
print(n_games_by_age)

