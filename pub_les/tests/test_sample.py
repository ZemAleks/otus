def test_running(database):
    result = "Running test data service setup - запуск службы настройки тестовых данных."
    assert result
    print(result)   # результат, который вернул тест


def test_db(connect_to_database):
    status_down = "bus connection status - статус подключения к шине БД."
    print(status_down)
    assert status_down
    print(status_down)


def test_time():
    x, y, summ = 1, 2, 3
    assert x + y == summ
    print(f"Test time - время прохождения теста {summ} = sec.")


def test_connect(rest_service):  # Прокидываем фикстуру в тест и она выполнится перед тестом
    status_connect = "Database connection established - Соединение с базой данных установлено."
    assert status_connect
    print(status_connect)  # Используем фикстуру, она вернет нам текст с подключением к БД



