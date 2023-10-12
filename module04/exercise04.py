import pickle

countries = [
    ("tur", "turkey", "asia", 80000000),
    ("fra", "france", "europe", 67000000),
    ("ita", "italy", "europe", 60000000)
]

with open("world.pkl", mode="wb") as file:
    pickle.dump(countries, file)
