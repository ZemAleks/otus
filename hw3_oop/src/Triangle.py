from Figure import Figure

"""
- Треугольник существует только тогда, когда сумма двух его сторон больше третьей. 
- Требуется сравнить каждую сторону с суммой двух других. 
- Если хотя бы в одном случае, любая сторона окажется больше, либо равна сумме двух других, 
- то треугольника с такими сторонами не существует.
"""


class Triangle(Figure):

    def __init__(self, side_a, side_b, side_c):
        super().__init__
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.get_semiperimeter = (side_a + side_b + side_c) / 2  # расчет полупериметра - s
        self.get_perimeter = side_a + side_b + side_c  # расчет периметра - p
        self.sem_a = self.get_semiperimeter - side_a  # расчет значения (s-a) для стороны - а
        self.sem_b = self.get_semiperimeter - side_b  # расчет значения (s-b) для стороны - b
        self.sem_c = self.get_semiperimeter - side_c  # расчет значения (s-c) для стороны - c

        if side_a + side_b <= side_c:
            raise ValueError("Треугольник не может быть создан")
        elif side_a + side_c <= side_b:
            raise ValueError("Треугольник не может быть создан")
        elif side_b + side_c <= side_a:
            raise ValueError("Треугольник не может быть создан")
        else:
            self.name = f"Три стороны треугольника {side_a}, {side_b} и {side_c}"

    # расчет площади: area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    @property
    def get_area(self):
        return (self.get_semiperimeter * self.sem_a * self.sem_b * self.sem_c) ** 0.5

    # расчет полупериметра: s = (a + b + c) / 2
    def get_semiperimeter(self):
        return self.get_semiperimeter

    # Периметр находится путем сложения длин всех сторон треугольника
    # расчет периметра: p = a + b + c
    def get_perimeter(self):
        return self.get_perimeter

    def __str__(self):
        return f"Треугольник с площадью {self.get_area}, периметром {self.get_perimeter}, полупериметром {self.get_semiperimeter} со сторонами {self.side_a}, {self.side_b} и {self.side_c}"

    @get_area.setter
    def get_area(self, value):
        self._get_area = value


r = Triangle(3, 5, 6)
print(Triangle)
print(Triangle.get_area)
print(r)
