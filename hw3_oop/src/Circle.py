from hw3_oop.src.Figure import Figure


class Circle(Figure):
    """
    - Геометрическая фигура Окружность.
    - Окружность — замкнутая плоская кривая, все точки которой равноудалены от заданной точки,
    - лежащей в той же плоскости, что и кривая: эта точка называется центром окружности.
    - Отрезок, соединяющий центр с какой-либо точкой окружности, называется радиусом.
    - Радиусом называется также и длина этого отрезка.
    """

    def __init__(self, axis_x: int, axis_y: int, radius: int):
        super().__init__()
        # Type hints — это подсказки типов данных в Python, чтобы контролировать типы данных.
        # Для указания типов атрибутов класса используйте аннотации типов и __init__ метод.
        self.axis_x: int = axis_x  # координата центра окружности по оси x
        self.axis_y: int = axis_y  # координата центра окружности по оси y
        self.radius: int = radius
        self.pi = 3.14  # число Пи, равное π = 3.14
        self.name = f"Circle"  # имя, название геометрической фигуры

        # axis_x и axis_y координаты центра окружности, по умолчанию центр находится в (0, 0).
        if axis_x != 0 or axis_y != 0:
            raise ValueError("Окружность не может быть создана.")
        elif radius <= 0:
            raise ValueError("Окружность не может быть создана.")

    # Если формулу указывать в методе, то Площадь будет вычисляться динамически при вызове.
    def get_area(self) -> float:
        return self.pi * self.radius * self.radius  # расчет площади круга: get_area = π * r ** 2

    # Если формулу указывать в методе, то Периметр будет вычисляться динамически при вызове.
    def get_perimeter(self) -> float:
        return 2 * self.pi * self.radius  # расчет длины окружности: length = 2πr

    def __str__(self) -> str:
        return (f"Площадь круга: {'{:.2f}'.format(self.get_area())}, "
                f"периметр или длина окружности: {'{:.2f}'.format(self.get_perimeter())}")


# c = Circle(0, 0, 4)
#
# print(Circle.add_area)
# print(Circle)
# print(Circle.get_area)
# print(c)
#
# print(c.add_area(c))
# print(c.name)
# print(c.__doc__)   # вызвать строку документации docstring
