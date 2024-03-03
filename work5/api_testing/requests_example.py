import requests
import pprint
import json

BASE_URL_PETSTORE = 'https://petstore.swagger.io/v2'      # базовый адрес URL ресурса.

# Основной набор методов библиотеки requests.

# Метод GET.
# Объявление объекта response с информацией по запросу.
response = requests.get(f'{BASE_URL_PETSTORE}/pet/1')   # вызываем метод GET и указываем URL адрес, передаем данные в теле запроса.

# Построчный вывод информации с ответами по запросу.
pprint.pprint('GET example')     # вывод строки с методом и названием запроса для информации, текстом "ПОЛУЧИТЬ пример с ответом запроса".
pprint.pprint(response.url)      # вывод строки с url адресом запроса.
pprint.pprint(response.status_code)     # вывод статус кода ответа в числовом формате.
pprint.pprint(response.reason)      # вывод строки с текстовой информацией об описании статус кода.
pprint.pprint(response.text)       # вывод строки с информацией о запросе в текстовом формате из тела ответа (body response).
pprint.pprint(response.json())       # вывод строки с информацией о запросе в виде словаря json из тела ответа (body response).
pprint.pprint('**********')
# comment
# Get with filters - Получить с фильтрами.
# get https://petstore.swagger.io/v2/pet?bod=20220506&breed=corgi
pass

# Метод POST - создание объекта или в данном случае обновление информации объекта.
# С помощью запроса Post, переименовываем имя питомца на Barsic.
data = {'name': 'Barsic'}      # Объявление объекта data, с информацией о теле запроса (request body) для отправки значений на сервер.
response = requests.post(f'{BASE_URL_PETSTORE}/pet/1', data=data)   # Вызываем метод Post и указываем URL адрес,
# передаем данные в объекте data, в качестве тела запроса (body request).

pprint.pprint('POST example')        # вывод строки с методом и названием запроса для информации, текстом "ПОЛУЧИТЬ пример с ответом запроса".
pprint.pprint(response.status_code)      # вывод статус кода ответа в числовом формате.
pprint.pprint(response.reason)      # вывод строки с текстовой информацией об описании статус кода.

dict_text = json.loads(response.text)   # Объявление объекта dict_text, преобразовывает текст в json используя метод json.loads,
# который передает значения {'code': 200, 'message': '1', 'type': 'unknown'}, тоже самое что метод response.json().
pet_id = dict_text['message']   # Объявление объекта pet_id, передает значение идентификатора pet_id, которое хранится в поле message (сообщение).
pprint.pprint(f'GET pet_id:  {pet_id}')      # вывод строки с информацией об идентификаторе объекта питомца pet_id.

# Проверяем информацию (verify post) на сервере, по идентификатору pet_id нового объекта животного,
# после выполненного Post запроса на создание или обновление объекта на сервере в базе данных.
response = requests.get(f'{BASE_URL_PETSTORE}/pet/{pet_id}')    # Вызываем метод Get и указываем URL адрес, передает данные идентификатора в endpoint URL.

pprint.pprint(f'GET {pet_id}')      # вывод строки с информацией по идентификатору объекта питомца pet_id с именем Barsic.
pprint.pprint(response.status_code)     # вывод статус кода ответа в числовом формате.
pprint.pprint(response.text)       # вывод строки с информацией о запросе в текстовом формате из тела ответа (body response).

pet_info = json.loads(response.text)    # Объявление объекта pet_info, запросили словарь json в формате текста с информацией об объекте.
assert data['name'] == pet_info['name']     # сравниваем значения Имени, изначальное и текущее имя у объекта.
assert data['name'] == response.json()['name']
pprint.pprint('**********')
# comment
# POST, PATCH, PUT
pass

# DELETE
response = requests.delete(f'{BASE_URL_PETSTORE}/pet/1')

pprint.pprint('DELETE example')
pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)

response = requests.get(f'{BASE_URL_PETSTORE}/pet/1')
pprint.pprint(f'GET 1')

pprint.pprint(response.status_code)
pprint.pprint(response.reason)
pprint.pprint(response.text)
pprint.pprint('**********')
pass