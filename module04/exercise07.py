import json

with open("world.json", mode="rt") as file:
    countries = json.load(file)
    for country in countries:
        print(country)
