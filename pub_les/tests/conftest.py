import pytest


<<<<<<< HEAD
@pytest.fixture(scope="function")
=======
@pytest.fixture()
>>>>>>> 3c779fa (added fixtures to the file conftest.py)
def rest_service():
    print("Setting up REST service - Настройка REST-сервиса")
    yield
    print("Shutting down REST service - Отключение службы REST")


@pytest.fixture()
def connect_to_database():
<<<<<<< HEAD
    connection = "- Connection process started - code status 200"
=======
    connection = "- Connection process started -"
>>>>>>> 3c779fa (added fixtures to the file conftest.py)
    return connection


@pytest.fixture()
def database():
    print("Setting up database - Настройка базы данных")
    yield
    print("Shutting down database - Выключение базы данных")
