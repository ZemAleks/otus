import pytest


@pytest.fixture()
def rest_service():
    print("Setting up REST service - Настройка REST-сервиса")
    yield
    print("Shutting down REST service - Отключение службы REST")


@pytest.fixture()
def connect_to_database():
    connection = "- Connection process started -"
    return connection


@pytest.fixture()
def database():
    print("Setting up database - Настройка базы данных")
    yield
    print("Shutting down database - Выключение базы данных")
