## Домашнее задание

Работа с тестовыми данными.

### Цель:

Научиться работать с различными типами файлов.

### Описание/Пошаговая инструкция выполнения домашнего задания.

Работа с тестовыми данными
- 1.) Скачать файлы:
> https://github.com/konflic/front_example/blob/master/data/books.csv
> https://github.com/konflic/front_example/blob/master/data/users.json.
- 2.) Написать скрипт, который из двух данных файлов будет читать данные и на их основании создаст result.json файл со
  структурой:
> https://github.com/konflic/front_example/blob/master/data/reference.json.
- 3.) Идея в том что нужно раздать все книги из csv файла пользователям из списка.
  Книги складываются в виде словарей в массив books у каждого пользователя.
- 4.) Книг изначально больше чем пользователей, поэтому раздавать нужно по принципу "максимально поровну",
  т.е. если книг, например 10. а пользователей 3 то распределение будет таким - 4 3 3 (один получит оставшуюся книгу).
- 5.) Итоговая структура должна соответствовать стандарту json и парситься соответствующей библиотекой.

### Критерии оценки:

1. Задание оформить отдельным pull-request'ом, пример оформления по ссылке: https://www.youtube.com/watch?v=swWqJBFpaNY
2. В репозитории отсутствуют лишние файлы.
3. Соблюдается минимальный кодстайл (встроенный в PyCharm).
4. В личном кабинете или репозитории приложен файл result.json с итоговым результатом.
5. Исходные файлы копировать не нужно.