import csv
from csv import DictReader

from files import CSV_FILE

with open(CSV_FILE, newline='') as f:
    reader = csv.reader(f)

    header = next(reader)   # Извлекаем заголовок

    for row in reader:  # Итерируемся по данным делая из них словари
        print(row)      # print(dict(zip(header, row)))


with open(CSV_FILE, newline='') as f:
    reader = DictReader(f)

    # Итерируемся по данным делая из них словари
    for row in reader:
        print(row)