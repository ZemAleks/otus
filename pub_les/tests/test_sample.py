<<<<<<< HEAD
def test_one(rest_service):
    result = "service setup test data"
    assert result
    print(result)
    # print(rest_service) # результат, который вернул тест
=======

def test_one(rest_service):
    print("service setup test data")
>>>>>>> 3c779fa (added fixtures to the file conftest.py)


def test_two(database):
    x, y, summ = 1, 2, 3
    assert x + y == summ
    print("result = ", summ, "sec")

<<<<<<< HEAD

=======
>>>>>>> 3c779fa (added fixtures to the file conftest.py)
def test_three():
    assert "something"


def test_connect(connect_to_database):  # Прокидываем фикстуру в тест и она выполнится перед тестом
<<<<<<< HEAD
    print(connect_to_database)  # Используем фикстуру, она вернет нам текст с подключением к БД
    print("Database connection established")
=======
        print(connect_to_database)  # Используем фикстуру, она вернет нам текст с подключением к БД
        print("Database connection established")

>>>>>>> 3c779fa (added fixtures to the file conftest.py)
