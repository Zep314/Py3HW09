import csv

def quadratic_roots_decorator(func):
    def wrapper(filename):
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            reader.__next__()
            for row in reader:
                if len(row) == 3:
                    a, b, c = map(float, row)
                    print(f"Input: {a}x^2 + {b}x + {c} = 0")
                    func(a, b, c)
                    print("-----------------")
    return wrapper

@quadratic_roots_decorator
def find_quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        print("Two distinct real roots:")
        print(f"Root 1: {root1}")
        print(f"Root 2: {root2}")
    elif discriminant == 0:
        root = -b / (2*a)
        print("One real root:")
        print(f"Root: {root}")
    else:
        real_part = -b / (2*a)
        imaginary_part = (-discriminant)**0.5 / (2*a)
        print("Two complex roots:")
        print(f"Root 1: {real_part} + {imaginary_part}i")
        print(f"Root 2: {real_part} - {imaginary_part}i")

# Пример использования декоратора
file_path = "numbers.csv"
find_quadratic_roots(file_path)
