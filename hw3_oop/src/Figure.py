from abc import ABC, abstractmethod


class Figure(ABC):

    # размеры сторон фигуры: длина, ширина, высота

    def __init__(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    def add_area(self, other_figure: int):
        if not isinstance(other_figure, Figure):
            raise AssertionError("Can't add area")
        return self.get_area() + other_figure.get_area()
