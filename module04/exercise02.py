countries = [
    ("tur", "turkey", "asia", 80000000),
    ("fra", "france", "europe", 67000000),
    ("ita", "italy", "europe", 60000000)
]

with open("world.txt", mode="wt") as world:
    for code, name, continent, population in countries:
        world.write(f"{code},{name},{continent},{population}\n")
