class square:
    def __init__(self, edge: float) -> None:
        self.__edge = edge

    @property
    def edge(self) -> float:
        return self.__edge

    def area(self) -> float:
        return self.__edge * self.__edge

    def __str__(self) -> str:
        return f"square(edge: {self.edge})"


class cube(square):
    def __init__(self, edge: float) -> None:
        super().__init__(edge)

    def area(self) -> float:
        return 6 * self.edge * self.edge

    def __str__(self) -> str:
        return f"cube(edge: {self.edge})"


square_1 = square(10)
print(square_1)
print(f"Area is {square_1.area()}")
cube_1 = cube(20)
print(cube_1)
print(f"Area is {cube_1.area()}")



