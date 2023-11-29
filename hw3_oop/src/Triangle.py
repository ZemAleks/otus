from hw3_oop.src.Figure import Figure


class Triangle(Figure):
    """
    - Геометрическая фигура Треугольник.
    - Треугольник существует только тогда, когда сумма двух его сторон больше третьей.
    - Требуется сравнить каждую сторону с суммой двух других.
    - Если хотя бы в одном случае, любая сторона окажется больше, либо равна сумме двух других,
    - то треугольника с такими сторонами не существует.
    """

    def __init__(self, side_a: int, side_b: int, side_c: int):
        super().__init__()
        # Type hints — это подсказки типов данных в Python, чтобы контролировать типы данных.
        # Для указания типов атрибутов класса используйте аннотации типов и __init__ метод.
        self.side_a: int = side_a
        self.side_b: int = side_b
        self.side_c: int = side_c
        self.name = f"Triangle"  # имя, название геометрической фигуры

        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Треугольник не может быть создан.")
        elif side_a + side_b <= side_c:
            raise ValueError("Треугольник не может быть создан.")
        elif side_a + side_c <= side_b:
            raise ValueError("Треугольник не может быть создан.")
        elif side_b + side_c <= side_a:
            raise ValueError("Треугольник не может быть создан.")

    @property
    # расчет полупериметра треугольника s = (side_a + side_b + side_c) / 2
    def get_semiperimeter(self) -> float:
        return (self.side_a + self.side_b + self.side_c) / 2  # расчет полупериметра треугольника

    @property
    def sem_a(self) -> float:
        return self.get_semiperimeter - self.side_a  # расчет значения (s-a) для стороны - а

    @property
    def sem_b(self) -> float:
        return self.get_semiperimeter - self.side_b  # расчет значения (s-b) для стороны - b

    @property
    def sem_c(self) -> float:
        return self.get_semiperimeter - self.side_c  # расчет значения (s-c) для стороны - c

    # расчет периметра треугольника p = a + b + c
    def get_perimeter(self) -> int:
        return self.side_a + self.side_b + self.side_c  # расчет периметра треугольника p = a + b + c

    # расчет площади треугольника: get_area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    def get_area(self) -> int:
        return (self.get_semiperimeter * self.sem_a * self.sem_b * self.sem_c) ** 0.5

    def __str__(self) -> str:
        return (f"Треугольник с площадью: {'{:.2f}'.format(self.get_area())}, периметром: {self.get_perimeter()}, "
                f"полупериметром: {self.get_semiperimeter}, со сторонами: {self.side_a}, {self.side_b} и {self.side_c}.")


# t = Triangle(3, 5, 7)
#
# print(Triangle)
# print(Triangle.get_area)
# print(t)
#
# print(f'Площадь: {"{:.2f}".format(t.get_area())}, Периметр: {t.get_perimeter()}, расчет сторон а: {t.sem_a}, b: {t.sem_b}, c: {t.sem_c}.')
# print(t.add_area(t))
# print(t.name)
# print(t.__doc__)   # вызвать строку документации docstring
