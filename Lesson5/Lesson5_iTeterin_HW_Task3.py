# 3. Создать текстовый файл (не программно). Построчно записать
# фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч,
# вывести фамилии этих сотрудников. Выполнить подсчёт средней
# величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

def find_pay_more_20k_and_average_income(file):
    pay_list = list()
    while (line := file.readline().rstrip()):
        line_list = [x for x in line.split()]
        pay_list.append(float(line_list[1]))
        if float(line_list[1]) >= 20000:
            print(
                f'У {line_list[0]} оклад больше 20000, составляет - {line_list[1]}')
    print(f"Средний доход: {sum(pay_list)/len(pay_list)}")


def find_average_income():
    pass


def main():
    file_data = open('./Lesson5/lesson5_Task3.txt', 'r', encoding="utf-8")
    find_pay_more_20k_and_average_income(file_data)


if __name__ == '__main__':
    print("Задание №3")
    main()
