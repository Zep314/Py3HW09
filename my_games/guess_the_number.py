# Функция загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Функция должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT) 

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
MAX_TRY = 10


def guess_the_number():
    """
    Функция загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
    :return:
    """
    num = randint(LOWER_LIMIT, UPPER_LIMIT)
    print(f"Угадай число от {LOWER_LIMIT} до {UPPER_LIMIT}, которое я задумало")
    inp = -1
    turn_left = MAX_TRY
    while (turn_left >= 0) and (inp != num):  # Рабочий цикл
        inp = int(input('Введите число: '))
        if (inp < LOWER_LIMIT) or (inp > UPPER_LIMIT):
            print(f"Ошибка ввода! Вводите числа от {LOWER_LIMIT} до {UPPER_LIMIT}")
        else:
            if inp != num:
                print(f"Задуманное число {'больше' if num > inp else 'меньше'} {inp}." 
                      f" Осталось {turn_left} попыток")
            else:
                break
            turn_left -= 1
    if inp != num:
        print(f"Вы проиграли! Задуманное число было: {num}")
    else:
        print(f"Вы выиграли! Число {num} угадано верно!")
