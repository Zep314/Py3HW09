"""
Init-файл для пакета с моими модулями
"""
from my_utils2.my_math import find_roots
from my_utils2.my_files import generate_csv
from my_utils2.my_files import my_read_csv
from my_utils2.my_files import quadratic_equation_decorator

# Эти функции будем "экспортировать" для внешней работы
__all__ = ['find_roots', 'generate_csv', 'my_read_csv', 'quadratic_equation_decorator']
