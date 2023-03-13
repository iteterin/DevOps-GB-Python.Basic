# 6. Реализовать два небольших скрипта:
#    итератор, генерирующий целые числа, начиная с указанного;
#    итератор, повторяющий элементы некоторого списка, определённого заранее.
#
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Предусмотрите условие его завершения. #### Например, в первом задании
# выводим целые числа, начиная с 3. При достижении числа 10 — завершаем цикл.
# Вторым пунктом необходимо предусмотреть условие, при котором повторение
# элементов списка прекратится.

import sys
from itertools import count
from itertools import cycle


def input_list() -> list:
    print("Введите элементы списка через пробел в одну строчку (например: 1 10 1010):")
    line = sys.stdin.readline().rstrip()
    line = [int(x) for x in line.split()]
    return line


def generate_integers_from_n_to_j():
    print('Итератор, генерирующий целые числа, начиная с указанного')
    n = int(input("Введите целое число, с которого начать генерацию: "))
    j = int(input("Введите целое число, на котором остановить генерацию: "))
    number_list = list()
    for i in count(n):
        if i > j:
            break
        else:
            number_list.append(i)
    return number_list


def generate_list_items_repeated_n_times() -> list:
    repeat_list = input_list()
    generated_list = list()
    n = int(input(
        f"Введите кол-во посторений элементов списка - {repeat_list}: ")) * len(repeat_list)
    j = 1
    for i in cycle(repeat_list):
        if j > n:
            break
        else:
            generated_list.append(i)
            j += 1
    return generated_list


def main():
    # print(generate_integers_from_n_to_j())
    print(generate_list_items_repeated_n_times())


if __name__ == '__main__':
    print("Задание №6")
    main()
