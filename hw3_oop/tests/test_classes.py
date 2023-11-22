from src.Rectangle import Rectangle, Square, Circle
import pytest


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(4, 6, 24, 20),
                          (5, 10, 50, 30)])
def test_rectangle(side_a, side_b, area, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.name == f"Rectangle {side_a} and {side_b}"
    assert r.get_area() == area
    assert r.get_perimeter == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(-4, -6, 24, -20),
                          (0, 0, 0, 0),
                          (5, 10, 50, 30)])
def test_rectangle_negative(side_a, side_b, area, perimeter):
    with pytest.raises(ValueError):
        r = Rectangle(side_a, side_b)
        assert r.name == f"Rectangle {side_a} and {side_b}"
        assert r.get_area() == area
        assert r.get_perimeter == perimeter


@pytest.mark.parametrize(("side_a", "area", "perimeter"),
                         [(4, 16, 16),
                          (5, 25, 20)])
def test_sq(side_a, area, perimeter):
    r = Square(side_a)
    assert r.name == f"Square {side_a}"
    assert r.get_area() == area
    assert r.get_perimeter == perimeter


def test_add_area():
    r = Rectangle(2, 5)
    s = Square(5)
    assert r.add_area(s) == 35


def test_add_area_negative():
    r = Rectangle(2, 5)
    c = Circle(10)
    assert c.add_area(r) == 15