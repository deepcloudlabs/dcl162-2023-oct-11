import random
import math


class square:
    def __init__(self, edge: float) -> None:
        self.__edge = edge

    @property
    def edge(self) -> float:
        return self.__edge

    def area(self) -> float:
        print("square::area")
        return self.__edge * self.__edge

    def __str__(self) -> str:
        return f"square(edge: {self.edge})"


class cube(square):
    def __init__(self, edge: float) -> None:
        super().__init__(edge)

    def area(self) -> float:
        print("cube::area")
        return 6 * self.edge * self.edge

    def __str__(self) -> str:
        return f"cube(edge: {self.edge})"


class circle(square):
    def __init__(self, edge: float) -> None:
        super().__init__(edge)

    @property
    def radius(self) -> float:
        return self.edge / 2

    def area(self) -> float:
        print("circle::area")
        return math.pi * self.radius * self.radius

    def __str__(self) -> str:
        return f"circle(radius: {self.radius})"


shape = None
if random.randint(0, 2) == 0:
    shape = square(10)
elif random.randint(0, 2) == 1:
    shape = cube(20)
else:
    shape = circle(30)
print(type(shape))
print(f"area is {shape.area()}")
