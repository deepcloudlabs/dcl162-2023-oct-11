with open("world.txt", mode="rt") as world:
    for line in world:
        code, name, continent, population = line.strip().split(",")
        population = int(population)
        print(f"{code},{name},{continent},{population}")
