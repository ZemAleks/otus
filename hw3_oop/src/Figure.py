from abc import ABC, abstractmethod


class Figure(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    # Каждая фигура должна реализовать метод add_area(figure),
    # который должен принимать другую геометрическую фигуру и возвращать сумму площадей этих фигур.
    # Функция isinstance() вернет True, если проверяемый объект является экземпляром указанного класса (классов).
    # Функция, проверяет объект, который передается первым аргументом, на принадлежность к классу другого объекта.
    # Если объект object не является экземпляром данного типа, то функция всегда возвращает False.
    def add_area(self, other_figure) -> int:
        if not isinstance(other_figure, Figure):
            raise ValueError("Can't add area - Не могу добавить площадь")
        return self.get_area() + other_figure.get_area()
