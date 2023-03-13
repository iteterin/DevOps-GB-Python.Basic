# 4. Представлен список чисел. Определите элементы списка,
# не имеющие повторений. Сформируйте итоговый массив чисел,
# соответствующих требованию. Элементы выведите в порядке их
# следования в исходном списке.
# Для выполнения задания обязательно используйте генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

from os import sys


def input_data() -> list:
    print('Введите исходный список(например:2 2 2 7 23 1 44 44 3 2 10 7 4 11):')
    line = sys.stdin.readline().rstrip()
    line = [int(x) for x in line.split()]
    return line


def edit_the_list_without_repeat(s_list) -> list:
    new_list = [s_list[i]
                for i in range(0, len(s_list)) if s_list.count(s_list[i]) == 1]
    return new_list


def main():
    source_list = input_data()
    print(f'Исходный список: {source_list}')
    print(f'Измененный список: {edit_the_list_without_repeat(source_list)}')


if __name__ == '__main__':
    print("Задание №4")
    main()