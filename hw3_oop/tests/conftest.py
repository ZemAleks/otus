import pytest


@pytest.fixture(scope="session", autouse=True)
# инициализация и поднятие сервиса
def rest_service():
    print("\nSetting up REST service - Настройка REST-сервиса.")  # setup
    yield
    print("\nShutting down REST service - Отключение службы REST.")  # teardown


@pytest.fixture(scope="session", autouse=True)
# подключение и соединение с сервисом
def connect_to_server(rest_service):
    print("\nCode status 200 - connection successful - Статус кода 200 – соединение успешное.")
    yield
    print("\nSuccessfully disconnecting a connection from a database - Успешное отключение от базы данных.")


@pytest.fixture(scope="session", autouse=True)
# настройка и подключение к базе данных
def database(connect_to_server):
    print("\nSetting up database - Запущен процесс подключения к базе данных.")
    yield
    print("\nShutting down database - Запущен процесс отключение от базы данных.")


@pytest.fixture(scope="session", autouse=True)
# отправка размеров сторон прямоугольника из базы данных
def get_rectangle_from_db(database):
    def _wrapper(rectangle_sides: str):
        if rectangle_sides == "integer":
            return 3, 5, 3, 5
        elif rectangle_sides == "float":
            return 3.5, 5.5, 3.5, 5.5
    print("\nЗапуск процесса загрузки размеров сторон прямоугольника из базы данных.")
    yield _wrapper
    print("\nЗавершение процесса загрузки размеров сторон прямоугольника из базы данных.")