import csv
from random import randint

MIN_LIMIT = -100
MAX_LIMIT = 100
FILE_HEADER = ['A', 'B', 'C']


def generate_csv(filename, amount):
    if filename:
        with open(filename, 'w', encoding='UTF-8') as f:
            writer = csv.DictWriter(f, fieldnames=FILE_HEADER)
            writer.writeheader()
            writer.writerows([{'A': randint(MIN_LIMIT, MAX_LIMIT),
                               'B': randint(MIN_LIMIT, MAX_LIMIT),
                               'C': randint(MIN_LIMIT, MAX_LIMIT)} for _ in range(amount)]
                             )


def my_read_csv(filename):
    if filename:
        with open(filename, 'r', encoding='UTF-8') as f:
            reader = csv.DictReader(f)
            return [{k: int(v) for k, v in d.items()} for d in [row for row in reader]]


def quadratic_equation_decorator(func):
    def wrapper(*args, **kwargs):
        with open('numbers3.csv', 'r', encoding='UTF-8') as f:  ###!!!!!!!!!!
            reader = csv.DictReader(f)
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                print(f"Корни уравнения {a}x^2 + {b}x + {c}: {result}")

        return wrapper
