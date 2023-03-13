# 5. Создать (программно) текстовый файл, записать в
# него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле
# и выводить её на экран.


def int_r(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num


def generate_file(filename):
    out_file = open(filename, "w", encoding='utf-8')
    out_file.write("10 14 45 109 29 66 75 263 10.2 385.67")
    out_file.close()


def sum_digit_from_file(filename):
    with open(filename, 'r', encoding='UTF-8') as file:
        while (line := file.readline().rstrip()):
            result = [float(x) for x in line.split()]
    print(f'Результат: {sum(result)}')
    print(f'Результат с округлением: {int_r(sum(result))}')


def main():
    filename = './Lesson5/lesson5_Task5.txt'
    generate_file(filename)
    sum_digit_from_file(filename)


if __name__ == '__main__':
    print("Задание №5")
    main()
