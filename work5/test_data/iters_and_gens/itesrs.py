class MyNumbers:
    def __init__(self, maxi=0):
        self.maxi = maxi

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n > self.maxi:
            raise StopIteration
        else:
            result = self.n
            self.n += 1
            return result


my_numbers = MyNumbers(4)
my_iter = iter(my_numbers)

while True:
    try:
        print(next(my_iter))
    except StopIteration:
        break

# for i in my_iter:
#     print(i)

# for i in MyNumbers(4):
#     print(i)
