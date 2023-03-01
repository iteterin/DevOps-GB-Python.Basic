# 4. Программа принимает действительное положительное
# число x и целое отрицательное число y. Выполните
# возведение числа x в степень y. Задание реализуйте
# в виде функции my_func(x, y). При решении задания
# нужно обойтись без встроенной функции возведения
# числа в степень.
#
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **,
# предусматривающая использование цикла.

def input_data():
    error_msg = "Вы ввели данные не удвалитворяющие условию. Пожалуйста, попробуйте еще раз.."
    try:
        x = int(input("Введите целое действительное положительное число X: "))
        y = int(input("Введите целое отрицательное число Y: "))
    except:
        print(error_msg)
        main()

    if x > 0 and y < 0:
        return x, y
    else:
        print(error_msg)
        main()


def my_func_1(x, y):
    print(f'{x}^({y}) = {x**y}')


def my_func_2(x, y):
    temp_y = y
    result = 1
    while temp_y != 0:
        result *= x
        temp_y += 1
    print(f'{x}^({y}) = {1/result}')


def main():
    x, y = input_data()
    my_func_1(x=x, y=y)
    my_func_2(x=x, y=y)


if __name__ == '__main__':
    print("Задание №4")
    main()