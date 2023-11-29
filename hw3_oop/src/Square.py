from hw3_oop.src.Rectangle import Rectangle


class Square(Rectangle):
    """
    - Геометрическая фигура Квадрат.
    - Все четыре стороны квадрата имеют одинаковую длину, то есть они равны.
    - Противоположные стороны квадрата параллельны.
    - Сумма углов квадрата равна 360°.
    - Диагонали квадрата имеют одинаковые длины.
    - При инициализации класс потомок Square(Rectangle) берет от родительского класса Rectangle(Figure) методы расчета:
    - площади (get_area), периметра (et_perimeter) и принимает другую фигуру для расчета суммы площадей (add_area).
    - Все методы для Квадрата наследуются от класса Прямоугольника.
    """

    def __init__(self, side_a: int, side_b: int, side_c: int, side_d: int):
        if side_a <= 0 or side_b <= 0 or side_c <= 0 or side_d <= 0:
            raise ValueError("Квадрат не может быть создан с нулевым или отрицательным значением для его сторон.")
        elif side_a != side_b or side_a != side_c or side_a != side_d:  # Если одна сторона квадрата не равна другой
            raise ValueError("Квадрат не может быть создан с введенным значением для его сторон.")

        super().__init__(side_a, side_a, side_a, side_a)
        # Type hints — это подсказки типов данных в Python, чтобы контролировать типы данных.
        # Для указания типов атрибутов класса используйте аннотации типов и __init__ метод.

        self.name = f"Square"  # имя, название геометрической фигуры

    def __str__(self) -> str:
        return (f"Квадрат с площадью: {'{:.0f}'.format(self.get_area())}, "
                f"периметром: {self.get_perimeter()}, с противоположными сторонами: {self.side_a} "
                f"и {self.side_b}")


sq = Square(10, 10, 10, 10)

print(Square)
print(Square.get_area(sq))
print(sq)
print(f'Название фигуры: {sq.name} - квадрат.')

print(sq.get_area())    # площадь
print(sq.side_a)
print(sq.add_area(sq))  # сумма площадей

print(sq.__doc__)   # вызвать строку документации docstring
print(dir(sq))   # выводит дандер - dunder (двойное подчеркивание) / magic методы
