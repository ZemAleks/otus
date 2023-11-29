import pytest


@pytest.fixture(scope="module", autouse=True)
def rest_service():
    print("Setting up REST service - Настройка REST-сервиса")   # инициализация и поднятие сервисов
    yield
    print("Shutting down REST service - Отключение службы REST")


@pytest.fixture()
def connect_to_database():
    connection = "Code status 200 - connection successful - Статус кода 200 – соединение успешное."
    return print(connection)


@pytest.fixture(scope="module", autouse=True)
def database():
    print("Setting up database - Настройка базы данных")
    yield
    print("Shutting down database - Отключение базы данных")




