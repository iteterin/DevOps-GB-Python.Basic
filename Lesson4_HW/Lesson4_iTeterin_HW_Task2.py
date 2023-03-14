# 2. Представлен список чисел. Необходимо вывести
# элементы исходного списка, значения которых
# больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию,
# оформить в виде списка. Для его формирования используйте генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

from os import sys


def edit_list_larger_than_prev(s_list) -> list:
    new_list = [s_list[i]
                for i in range(1, len(s_list)) if s_list[i] > s_list[i-1]]
    return new_list


def input_data() -> list:
    print('Введите исходный список(например:300 2 12 44 1 1 4 10 7 1 78 123 55):')
    line = sys.stdin.readline().rstrip()
    line = [int(x) for x in line.split()]
    return line


def main():
    source_list = input_data()
    print(f'Исходный список: {source_list}')
    print(f'Измененный список: {edit_list_larger_than_prev(source_list)}')


if __name__ == '__main__':
    print("Задание №2")
    main()
