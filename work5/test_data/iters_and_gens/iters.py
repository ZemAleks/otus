
"""
- Итератор (iterator) - это объект, который возвращает свои элементы по одному за раз.
- С точки зрения Python - это любой объект, у которого есть метод __next__.
- Этот метод возвращает следующий элемент, если он есть, или возвращает исключение StopIteration, когда элементы закончились.
- Кроме того, итератор запоминает, на каком объекте он остановился в последнюю итерацию.
- В Python у каждого итератора присутствует метод __iter__ - то есть, любой итератор является итерируемым объектом.
- Этот метод просто возвращает сам итератор.
"""


class MyNumbers:  # создаем Класс MyNumbers
    def __init__(self, maxi=0):  # метод, который инициализирует максимальное число
        self.maxi = maxi

    def __iter__(self):  # метод, который создает и итерирует бесконечный счетчик целых чисел
        self.counter = 0
        return self  # возвращает целые числа

    def __next__(self):  # который возвращает свои элементы по условию работы счетчика
        if self.counter > self.maxi:  # если не достиг максимума
            raise StopIteration  # когда достигаем максимум, вызываем остановку счетчика
        else:
            result = self.counter  # сохраняем полученный элемент
            self.counter += 1  # увеличиваем на единицу и перезаписываем
            return result  # возвращаем предыдущий элемент


my_numbers = MyNumbers(4)  # создаем объект, который должен возвращать 4 элемента
my_iter = iter(my_numbers)  # создаем итератор
while True:  # бесконечный цикл
    try:
        print(next(my_iter))
    except StopIteration:  # будем вызывать новый элемент, пока не получим исключение
        break

"""Примеры итераторов бесконечного цикла, которые позволяют создавать и работать с последовательностями объектов."""

# for i in my_iter:     # аналогичный пример бесконечного цикла, только упрощенный синтаксический сахар
#     print(i)

# for i in MyNumbers(4):     # так же можно сразу вызывать класс, так как цикл for запрашивает нужный метод
#     print(i)      # функция MyNumbers реализована через функцию range(), которая возвращает последовательность чисел

# for i in range(4):    # функция `range` возвращает объект, который генерирует значения на лету, что увеличивает объем памяти.
#     print(i)
