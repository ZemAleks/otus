from Figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def get_area(self):
        return 5
