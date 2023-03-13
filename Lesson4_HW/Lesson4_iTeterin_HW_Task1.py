# 1. Реализовать скрипт, в котором должна быть предусмотрена функция
# расчёта заработной платы сотрудника. Используйте в нём формулу:
# (выработка в часах*ставка в час) + премия. Во время выполнения
# расчёта для конкретных значений необходимо запускать скрипт с параметрами.
#
# Run: python3 Lesson4_iTeterin_HW_Task1.py 8 1000 500
# OutPut:
# Задание №1
# Заработная плата сотрудника: 8500

from sys import argv


def payroll_of_an_employee(working_out_in_hours, rate_per_hour, award):
    paycheck = working_out_in_hours * rate_per_hour + award
    print(f'Заработная плата сотрудника: {paycheck}')


print("Задание №1")
script_name, first_param, second_param, third_param = argv

payroll_of_an_employee(working_out_in_hours=int(
    first_param), rate_per_hour=int(second_param), award=int(third_param))


