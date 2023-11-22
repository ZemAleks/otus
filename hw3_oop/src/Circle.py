from hw3_oop.src.Figure import Figure


class Circle(Figure):
    """
    - Окружность — замкнутая плоская кривая, все точки которой равноудалены от заданной точки,
    - лежащей в той же плоскости, что и кривая: эта точка называется центром окружности.
    - Отрезок, соединяющий центр с какой-либо точкой окружности, называется радиусом.
    - Радиусом называется также и длина этого отрезка.
    """

    def __init__(self, side_a: int):
        super().__init__()
        self.pi: float = 3.14  # число Пи равное π = 3.14
        self.radius: int = side_a
        self.name = f"Circle"  # имя, название геометрической фигуры
        self.get_area: float = self.pi * self.radius * self.radius  # расчет площади круга: get_area = π * r ** 2
        self.get_perimeter: float = 2 * self.pi * self.radius  # расчет длины окружности: length = 2πr

    def get_area(self):
        return self.get_area

    def get_perimeter(self):
        return self.get_perimeter

    def __str__(self) -> str:
        return (f"Площадь круга: {'{:.2f}'.format(self.get_area)}, "
                f"периметр или длина окружности: {'{:.2f}'.format(self.get_perimeter)}")

# c = Circle(4)
# print(Circle.add_area)
# print(Circle)
# print(Circle.get_area)
# print(c)
# print(Circle.add_area)
# print(c.add_area)
# print(c.name)
