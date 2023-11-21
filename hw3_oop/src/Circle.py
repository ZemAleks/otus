from Figure import Figure


class Circle(Figure):
    """
    - Окружность — замкнутая плоская кривая, все точки которой равноудалены от заданной точки,
    - лежащей в той же плоскости, что и кривая: эта точка называется центром окружности.
    - Отрезок, соединяющий центр с какой-либо точкой окружности, называется радиусом.
    - Радиусом называется также и длина этого отрезка.
    """

    def __init__(self, radius: int):
        super().__init__()
        self.pi: float = 3.14  # число Пи равное π = 3.14
        self.radius: int = radius
        self.get_perimeter: float = 2 * self.pi * self.radius  # расчет длины окружности: length = 2πr
        self.name = f"Радиус окружности: {radius}"

    # расчет площади круга: area = π * r ** 2
    @property
    def get_area(self) -> float:
        return self.pi * self.radius * self.radius

    # расчет длины окружности: length = 2πr
    def get_perimeter(self) -> float:
        return self.get_perimeter

    def __str__(self) -> str:
        return (f"Площадь круга: {'{:.2f}'.format(self.get_area)}, "
                f"периметр или длина окружности: {'{:.2f}'.format(self.get_perimeter)}")


c = Circle(radius=5)
print(Circle)
print(Circle.get_area)
print(c)
