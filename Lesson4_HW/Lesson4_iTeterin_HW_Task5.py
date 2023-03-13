# 5. Реализовать формирование списка, используя функцию range()
# и возможности генератора. В список должны войти чётные числа
# от 100 до 1000 (включая границы). Нужно получить результат
# вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from os import sys
from functools import reduce


def get_product_even_elements() -> list:
    return reduce(lambda x, y: x*y, [i for i in range(100, 1000) if i % 2 == 0])


def main():
    print(f'Произведения всех элементов списка: {get_product_even_elements()}')


if __name__ == '__main__':
    print("Задание №5")
    main()
