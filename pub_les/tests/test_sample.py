def test_one(rest_service):
    a1, b1 = rest_service  # получение адрессов из фикстуры
    result = "Service setup test data - Данные тестовой настройки"
    assert result
    assert a1
    assert b1
    assert rest_service[0]  # взять первый элемент
    print(result)
    print(rest_service)
    print(rest_service[0])
    print(a1, b1)


def test_another():
    answer = 100 + 1
    assert answer
    print(answer)


def test_two(database):
    x, y, summ = 1, 2, 3
    assert x + y == summ
    print("result = ", summ, "sec")


def test_three(say_hello):
    answer = "validation response = something - твет проверки = что-нибудь"
    assert answer
    assert say_hello
    print(answer)
    print(say_hello)
    print("server response result, = ", say_hello, "код результат ответа сервера")


def test_connect(connect_to_database):  # Прокидываем фикстуру в тест и она выполнится перед тестом
    print(connect_to_database)  # Используем фикстуру, она вернет нам текст с подключением к БД
    print("Database connection established - Соединение с базой данных установлено")
