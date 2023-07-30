import pytest



@pytest.fixture(scope="function")
def rest_service():
    print("Setting up REST service - Настройка REST-сервиса")
    yield
    print("Shutting down REST service - Отключение службы REST")

    

@pytest.fixture()
def connect_to_database():
    connection = "- Connection process started - code status 200"



@pytest.fixture()
def database():
    print("Setting up database - Настройка базы данных")
    yield
    print("Shutting down database - Выключение базы данных")
