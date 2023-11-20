from Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side: int):
        if side <= 0:
            raise ValueError("Can't create Square")
        super().__init__(side, side)
        self.side_a: int = side
        self.name = f"Square {side}"
