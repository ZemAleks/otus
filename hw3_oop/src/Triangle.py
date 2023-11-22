from hw3_oop.src.Figure import Figure


class Triangle(Figure):
    """
    - Треугольник существует только тогда, когда сумма двух его сторон больше третьей.
    - Требуется сравнить каждую сторону с суммой двух других.
    - Если хотя бы в одном случае, любая сторона окажется больше, либо равна сумме двух других,
    - то треугольника с такими сторонами не существует.
    """

    def __init__(self, side_a: int, side_b: int, side_c: int):
        super().__init__()
        self.side_a: int = side_a
        self.side_b: int = side_b
        self.side_c: int = side_c
        self.name = f"Triangle"  # имя, название геометрической фигуры
        self.get_semiperimeter: float = (side_a + side_b + side_c) / 2  # расчет полупериметра треугольника
        self.get_perimeter: int = side_a + side_b + side_c  # расчет периметра треугольника p = a + b + c
        self.sem_a: float = self.get_semiperimeter - side_a  # расчет значения (s-a) для стороны - а
        self.sem_b: float = self.get_semiperimeter - side_b  # расчет значения (s-b) для стороны - b
        self.sem_c: float = self.get_semiperimeter - side_c  # расчет значения (s-c) для стороны - c
        # расчет площади треугольника: get_area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
        self.get_area: int = (self.get_semiperimeter * self.sem_a * self.sem_b * self.sem_c) ** 0.5

        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Треугольник не может быть создан.")
        elif side_a + side_b <= side_c:
            raise ValueError("Треугольник не может быть создан.")
        elif side_a + side_c <= side_b:
            raise ValueError("Треугольник не может быть создан.")
        elif side_b + side_c <= side_a:
            raise ValueError("Треугольник не может быть создан.")

    def get_area(self):
        return self.get_area

    def get_perimeter(self):
        return self.get_perimeter

    def __str__(self) -> str:
        return (f"Треугольник с площадью: {'{:.2f}'.format(self.get_area)}, периметром: {self.get_perimeter}, "
                f"полупериметром: {self.get_semiperimeter}, со сторонами: {self.side_a}, {self.side_b} и {self.side_c}")


# t = Triangle(3, 5, 6)
# print(Triangle)
# print(Triangle.get_area)
# print(t)
# print('{:.2f}'.format(t.get_area))
# print(t.add_area)
# print(t.name)
