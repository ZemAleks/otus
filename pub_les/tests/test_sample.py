<<<<<<< HEAD

def test_one(rest_service):
    print("service setup test data")


def test_two(database):
    x, y, summ = 1, 2, 3
    assert x + y == summ
    print("result = ", summ, "sec")

def test_three():
    assert "something"


def test_connect(connect_to_database):  # Прокидываем фикстуру в тест и она выполнится перед тестом
        print(connect_to_database)  # Используем фикстуру, она вернет нам текст с подключением к БД
        print("Database connection established")


