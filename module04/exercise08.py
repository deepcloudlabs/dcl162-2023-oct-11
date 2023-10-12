import csv

countries = [
    ("tur", "turkey", "asia", 80000000),
    ("fra", "france", "europe", 67000000),
    ("ita", "italy", "europe", 60000000)
]

with open("world.csv", mode="wt", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(countries)