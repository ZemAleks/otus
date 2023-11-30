from hw3_oop.src.Rectangle import Rectangle
from hw3_oop.src.Square import Square
from hw3_oop.src.Circle import Circle
import pytest

"""
- Тесты по настройки системы.
- Запускают конфигурационные файлы для настройки соединения с шиной.
- Запускают процессы CI разворачивают контейнеры и устанавливают тестовую среду.
"""


def test_time():
    x, y, summ = 1, 2, 3
    assert x + y == summ
    print(f"Test time - время прохождения настройки подключения {summ} = sec.")


def test_running(connect_to_database):
    result = "Running test data service setup - запуск службы настройки тестовых данных."
    assert result
    print(result)  # результат, который вернул тест


"""Конфигурационные тесты по настройке и подключению к базе данных"""


def test_connect(database):  # Прокидываем фикстуру в тест и она выполнится перед тестом
    status_connect = "Database connection established - Соединение с базой данных установлено."
    assert status_connect
    print(status_connect)  # Используем фикстуру, она вернет нам текст с подключением к БД


def test_db(rest_service):
    status_down = "bus connection status - статус подключения к шине БД."
    print(status_down)
    assert status_down
    status_up = "bus disconnect status - статус отключения от шины."
    print(status_up)


"""Тесты проверки проектного модуля системы создания Геометрических фигур."""


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "side_d", "area", "perimeter"),
                         [(4, 6, 4, 6, 24, 20),
                          (5, 10, 5, 10, 50, 30)])
def test_rectangle(side_a: int, side_b: int, side_c: int, side_d: int, area: int, perimeter: int):
    r = Rectangle(side_a, side_b, side_c, side_d)
    assert r.name == f"Rectangle"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "side_d", "area", "perimeter"),
                         [(-4, -6, 4, 6, 24, -20),
                          (0, 0, 0, 0, 0, 0),
                          (-5, 10, 5, 10, 50, 30)])
def test_rectangle_negative(side_a: int, side_b: int, side_c: int, side_d: int, area: int, perimeter: int):
    with pytest.raises(ValueError):
        r = Rectangle(side_a, side_b, side_c, side_d)
        assert r.name == f"Rectangle"
        assert r.get_area() == area
        assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "side_d", "area", "perimeter"),
                         [(4, 4, 4, 4, 16, 16),
                          (5, 5, 5, 5, 25, 20),
                          (3, 3, 3, 3, 9, 12)])
def test_sq(side_a: int, side_b: int, side_c: int, side_d: int, area: int, perimeter: int):
    r = Square(side_a, side_b, side_c, side_d)
    assert r.name == f"Square"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


def test_add_area():
    r = Rectangle(2, 5, 2, 5)
    s = Square(5, 5, 5, 5)
    assert r.add_area(s) == 35


def test_add_area_negative():
    with pytest.raises(ValueError):
        r = Rectangle(2, 5, 2, 5)
        c = Circle(0, 0, 4)
    assert c.add_area(r) == 15
