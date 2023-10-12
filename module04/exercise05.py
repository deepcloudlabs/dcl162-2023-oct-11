import pickle

with open("world.pkl", mode="rb") as file:
    countries = pickle.load(file)
    for country in countries:
        print(country)
