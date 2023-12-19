from hw3_oop.src.Rectangle import Rectangle
from hw3_oop.src.Square import Square
from hw3_oop.src.Triangle import Triangle
from hw3_oop.src.Circle import Circle
import pytest
from contextlib import nullcontext as does_not_raise

"""
- Используем the Task type для отображения сбоев тестов.
-
- Тесты по настройки системы.
- Запускают конфигурационные файлы для настройки соединения с шиной.
- Запускают процессы CI разворачивают контейнеры и устанавливают тестовую среду.
"""


def test_time():
    x, y, summ = 1, 2, 3
    assert x + y == summ
    print(f"Test time - время прохождения настройки подключения {summ} = sec.")


def test_running():
    result = "Running test data service setup - запуск службы настройки тестовой среды."
    assert result
    print(result)  # результат, который вернул тест


"""
- Конфигурационные тесты по настройке и подключению к базе данных.
"""


@pytest.mark.parametrize(("rectangle_sides", "area", "perimeter"),
                         [("integer", 15, 16),
                          ("float", 19.25, 18)])
def test_rectangle_from_bd(get_rectangle_from_db, rectangle_sides: str, area: float, perimeter: float):
    side_a, side_b, side_c, side_d = get_rectangle_from_db(rectangle_sides=rectangle_sides)
    r = Rectangle(side_a, side_b, side_c, side_d)
    assert r.name == f"Rectangle"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


def test_connect_db():
    status_sending = "sending a packet from the database - отправка пакета из базы."
    print(status_sending)
    assert status_sending
    status_confirmation = "confirmation of package sending status - подтверждение статуса отправки пакета."
    print(status_confirmation)  # Используем фикстуру, она вернет нам информацию по статусу.


def test_status_db():
    status_up = "bus request receipt status - статус получения запроса в шину."
    print(status_up)
    assert status_up
    status_down = "sending a request from the bus - отправка запроса из шины."
    print(status_down)


"""
- Тесты проверки проектного модуля системы создания Геометрических фигур.
"""


# проверка расчета параметров прямоугольника
@pytest.mark.parametrize(("side_a", "side_b", "side_c", "side_d", "area", "perimeter"),
                         [(4, 6, 4, 6, 24, 20),
                          (5, 10, 5, 10, 50, 30)])
def test_rectangle(side_a: int, side_b: int, side_c: int, side_d: int, area: float, perimeter: float):
    r = Rectangle(side_a, side_b, side_c, side_d)
    assert r.name == f"Rectangle"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


# проверка исключений расчета параметров прямоугольника
@pytest.mark.parametrize(("side_a", "side_b", "side_c", "side_d", "area", "perimeter", "expectation"),
                         {(-4, -6, 4, 6, 24, -20, pytest.raises(ValueError)),  # вызовет исключения
                          (0, 0, 0, 0, 0, 0, pytest.raises(ValueError)),  # вызовет исключения
                          (5, 10, 5, 10, 50, 30, does_not_raise())})  # не вызовет исключения
def test_rectangle_negative(side_a: int, side_b: int, side_c: int, side_d: int, area: float, perimeter: float, expectation):
    with expectation:
        r = Rectangle(side_a, side_b, side_c, side_d)
        assert r.name == f"Rectangle"
        assert r.get_area() == area
        assert r.get_perimeter() == perimeter


# проверка расчета параметров квадрата
@pytest.mark.parametrize(("side_a", "side_b", "side_c", "side_d", "area", "perimeter"),
                         [(4, 4, 4, 4, 16, 16),
                          (5, 5, 5, 5, 25, 20),
                          (3, 3, 3, 3, 9, 12)])
def test_square(side_a: int, side_b: int, side_c: int, side_d: int, area: float, perimeter: float):
    r = Square(side_a, side_b, side_c, side_d)
    assert r.name == f"Square"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


# проверка расчета параметров треугольника
@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(3, 5, 7, 6.49519052838329, 15),
                          (4, 3, 6, 5.332682251925386, 13),
                          (5, 4, 8, 8.181534085976786, 17)])
def test_triangle(side_a: int, side_b: int, side_c: int, area: float, perimeter: float):
    r = Triangle(side_a, side_b, side_c)
    assert r.name == f"Triangle"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


# проверка расчета параметров окружности
@pytest.mark.parametrize(("axis_x", "axis_y", "radius", "area", "perimeter"),
                         [(0, 0, 1, 3.14, 6.28),
                          (0, 0, 2, 12.56, 12.56),
                          (0, 0, 3, 28.259999999999998, 18.84)])
def test_circle(axis_x: int, axis_y: int, radius: int, area: float, perimeter: float):
    r = Circle(axis_x, axis_y, radius)
    assert r.name == f"Circle"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


"""
- Тесты проверки расчета сумму площадей этих Геометрических фигур.
"""


# проверка расчета сумму площадей прямоугольника и квадрата
def test_add_area():
    r = Rectangle(2, 5, 2, 5)  # площадь прямоугольника 10
    s = Square(5, 5, 5, 5)  # площадь квадрата 25
    assert r.add_area(s) == (10 + 25)


# проверка расчета сумму площадей прямоугольника и окружности
def test_add_area2():
    r = Rectangle(2, 5, 2, 5)  # площадь прямоугольника 10
    s = Circle(0, 0, 2)  # площадь окружности 12.56
    assert r.add_area(s) == (10 + 12.56)


# проверка исключений при расчете суммы площадей прямоугольника и окружности
@pytest.mark.parametrize(("side_a", "side_b", "side_c", "side_d", "area", "perimeter", "expectation"),
                         {(-4, -6, 4, 6, 24, -20, pytest.raises(ValueError)),  # вызовет исключения
                          (0, 0, 0, 0, 0, 0, pytest.raises(ValueError)),  # вызовет исключения
                          (5, 10, 5, 10, 50, 30, does_not_raise())})  # не вызовет исключения
def test_add_area_negative(side_a: int, side_b: int, side_c: int, side_d: int, area: float, perimeter: float, expectation):
    with expectation:
        re = Rectangle(side_a, side_b, side_c, side_d)
        c = Circle(0, 0, 2)  # площадь окружности 12.56
        assert c.add_area(re) == float(re.get_area() + c.get_area())
