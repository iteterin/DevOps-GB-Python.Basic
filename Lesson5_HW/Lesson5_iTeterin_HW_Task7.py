# 7. Создать вручную и заполнить несколькими
# строками текстовый файл, в котором каждая
# строка будет содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить
# прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней
# прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь
# с фирмами и их прибылями, а также словарь со средней
# прибылью. Если фирма получила убытки, также добавить
# её в словарь (со значением убытков).
# Пример списка:
# [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json


def generate_list_from_file(filename, json_filename):
    with open(filename, 'r', encoding='UTF-8') as f:
        lines = f.readlines()

    profit_dict = {}
    total_profit = 0
    count_profit = 0

    for line in lines:
        parts = line.split()
        name = parts[0]
        income = int(parts[2])
        expenses = int(parts[3])
        profit = income - expenses
        if profit >= 0:
            profit_dict[name] = profit
            total_profit += profit
            count_profit += 1
        else:
            profit_dict[name] = ['убыток', profit]

    average_profit = total_profit / count_profit

    result_list = [profit_dict, {'average_profit': average_profit}]
    print(result_list)
    with open(json_filename, 'w', encoding='UTF-8') as f:
        json.dump(result_list, f)


def main():
    filename = './Lesson5/lesson5_Task7.txt'
    json_filename = './Lesson5/lesson5_Task7_result.json'
    firms_data = generate_list_from_file(filename, json_filename)


if __name__ == '__main__':
    print("Задание №7")
    main()
