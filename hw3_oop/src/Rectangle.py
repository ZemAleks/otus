from hw3_oop.src.Figure import Figure


class Rectangle(Figure):
    """
    - Если три угла четырёхугольника прямые, то этот четырёхугольник является прямоугольником.
    - Если у прямоугольника одна из сторон меньше или равна нулю, то прямоугольник не может быть создан.
    - Противоположные стороны прямоугольника равны.
    - Квадрат – это прямоугольник, у которого все стороны равны.
    - Диагонали прямоугольника равны.
    - Точка пересечения диагоналей называется центром прямоугольника и также является центром описанной окружности.
    """

    def __init__(self, side_a: int, side_b: int, side_c: int, side_d: int):
        super().__init__()
        self.side_a: int = side_a
        self.side_b: int = side_b
        self.side_c: int = side_c
        self.side_d: int = side_d
        self.name: str = f"Rectangle"  # имя, название геометрической фигуры
        self.get_area: int = self.side_a * self.side_b  # расчет площади прямоугольника: get_area = a * b
        self.get_perimeter: int = 2 * (self.side_a + self.side_b)  # расчет периметра прямоугольника p = 2 * (a + b)

        if side_a <= 0 or side_b <= 0:
            raise ValueError("Прямоугольник не может быть создан.")
        elif side_a != side_c or side_b != side_d:  # Противоположные стороны прямоугольника не равны
            raise ValueError("Прямоугольник не может быть создан.")

    def get_area(self):
        return self.get_area

    def get_perimeter(self):
        return self.get_perimeter

    def __str__(self) -> str:
        return (f"Прямоугольник с площадью: {'{:.0f}'.format(self.get_area)}, "
                f"периметром: {self.get_perimeter}, с противоположными сторонами: {self.side_a} "
                f"и {self.side_b}")


# re = Rectangle(2, 4, 2, 4)
#
# print(Rectangle)
# print(Rectangle.get_area)
# print(re)
#
# print(re.side_a)
# print(re.add_area)
# print(re.name)
