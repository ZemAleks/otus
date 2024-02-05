import os


def get_path(file_name):     # функция, которая принимает имя файла
    work_folder = os.path.dirname(os.path.abspath(__file__))    # функция получает абсолютный путь до директории __file__
    return os.path.join(work_folder, file_name)     # объединяем абсолютный путь с именем папки используя параметр join
# Оператор join автоматически определяет ОС.
# Библиотека os.path автоматически подставляет разделитель при указании пути к файлам в директории, обратный или прямой слэш.
# Библиотека os выбирает необходимые правила указания пути, чтобы получился валидный путь, в рамках ОС на рабочей станции системы.


CSV_FILE = get_path('../books.csv')
JSON_FILE = get_path('../users.json')
JSON_FILE_W = get_path('../result.json')
