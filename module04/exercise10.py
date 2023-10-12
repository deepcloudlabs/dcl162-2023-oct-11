import pandas as pd

countries = [
    ("tur", "turkey", "asia", 80000000),
    ("fra", "france", "europe", 67000000),
    ("ita", "italy", "europe", 60000000)
]

df = pd.DataFrame(countries, columns=["code", "name", "continent", "population"])
df.to_csv("world_pandas.csv")
