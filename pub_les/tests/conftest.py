import pytest


@pytest.fixture(scope="function", autouse=True)
def rest_service():
    print("Setting up REST service - Настройка REST-сервиса")
    a = "code"
    b = 200
    yield a, b
    print("Shutting down REST service - Отключение службы REST")


@pytest.fixture
def say_hello(rest_service):
    a1, b1 = rest_service  # получение адрессов из фикстуры
    print("hello")
    return rest_service


@pytest.fixture()
def connect_to_database():
    connection = "- Connection process started - code status 200"


@pytest.fixture()
def database():
    print("Setting up database - Настройка базы данных")
    yield
    print("Shutting down database - Выключение базы данных")
