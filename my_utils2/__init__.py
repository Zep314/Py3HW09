"""
Init-файл для пакета с моими математическими и файловыми модулями
"""
from my_utils2.my_math import find_roots
from my_utils2.my_files import generate_csv
from my_utils2.my_files import my_read_csv
from my_utils2.my_files import find_roots_with_deco
from my_utils2.my_files import find_roots_with_2decos
from my_utils2.my_files import quadratic_equation_decorator
from my_utils2.my_files import save_to_json_decorator
from my_utils2.my_files import find_roots_with_all_decorators

# Эти функции будем "экспортировать" для внешней работы
__all__ = ['find_roots', 'generate_csv', 'my_read_csv', 'find_roots_with_deco',
           'find_roots_with_2decos', 'find_roots_with_all_decorators']
