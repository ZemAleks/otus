from Figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        super().__init__(radius)
        self.radius = radius
        self.name = f"Circle {radius}"

    def get_area(self):
        return 5
