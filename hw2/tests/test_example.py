import pytest
# frome helpers import print_green, print_cyan, print_blue

# what is a test? - Что такое тест?
# tests discovery. - Условия для обнаружения/открытие теста.
# pytest.mark.parametrize - Служебная марка parametrize.
# pytest fixture (scope, autouse)
# pass data from fixture into test
# conftest.py
# --setup-plan


# @pytest.mark.parametrize('a, b, result',
#                          [
#                              (1, 3, 4),
#                              (-1, 3, 2),
#                              (-1, -3, -4),
#                              (1, 0, 1),
#                          ])
# def test_sum(a, b, result):
#     assert a + b == result

# pytest fixture

class start_stop_rest_service():
    def test_one(start_stop_rest_service):
        print('This is test run')
    pass


def print_blue(self):
    pass

def print_green(self):
    pass

def print_cyan(self):
    pass

@pytest.fixture(scope='session', autouse=True)

def print_blue():
    print('Start Rest service')

# def print_green():
#     print_green('This is test run')

def start_stop_rest_service():
    print_blue('Start Rest service')
    yield
    print_blue('Stope Rest service')

def test_one():
    print_green('This is test run')

def test_two():
   print_green('This is test run')



