from functools import partial


def fun(x: int, y: int, z: int) -> int:
    return x ** y + z


cubed = lambda x: fun(x, 3, 0)
print(cubed(3))
numbers = [4, 8, 15, 16, 23, 42]
print(list(map(cubed, numbers)))
print(list(map(partial(fun, y=3, z=0), numbers)))
print(list(map(partial(fun, y=2, z=-1), numbers)))
