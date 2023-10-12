import operator
from functools import reduce

countries = [
    {"code": "tur", "name": "turkey", "continent": "asia", "population": 80_000_000},
    {"code": "fra", "name": "france", "continent": "europe", "population": 67_000_000},
    {"code": "ita", "name": "italy", "continent": "europe", "population": 60_000_000}
]

# imperative programming
total_population: int = 0
for country in countries:  # external loop -> iterator
    if country["continent"] == "europe":
        population: int = country["population"]
        total_population += population
print(f"total population of european countries is {total_population}")


def gun(u, v):
    return u ** 2 + v ** 3


fun = lambda u, v: u ** 2 + v ** 3
print(type(fun))
print(fun(3, 5))
print(type(gun))
print(gun(3, 5))
# declarative programming
# pipeline -> function composition -> higher-order function -> filter/map/reduce
to_population = lambda country: country["population"]


def fun_to_population(country):
    print(f"fun_to_population({country})")
    return country["population"]


is_european = lambda country: country["continent"] == "europe"


def fun_is_european(country):
    print(f"fun_is_european({country})")
    return country["continent"] == "europe"

def fun_sum(population, accumulated_population):
    print(f"fun_sum({population},{accumulated_population})")
    return population + accumulated_population

print(reduce(lambda s, u: s + u, map(to_population, filter(is_european, countries)), 0))
# internal loop -> pipeline -> filter/map -> i) HoF ii) Generator Function?
print(reduce(operator.add, map(to_population, filter(is_european, countries)), 0))
print(reduce(fun_sum, map(fun_to_population, filter(fun_is_european, countries)), 0))
#   countries -> filter -> map -> reduce -> solution!
#                 func     func   func
#            dict -> dict -> int -> int
"""
Higher Order Function ✔
Pure Function: stateless, no side effect -> lambda expression -> function ✔
Generator Function ✔
Partial Function ✔
"""

"""
  Data Parallesim
  Multi-Threaded
  ForkJoin Framework
  Thread Pool -> Job/Task Stealing Algorithms
"""
counter: int = 0


def sun(p, q):
    global counter
    counter += 1
    return p + q


run = lambda p, q: p + q
