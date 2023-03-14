# 1. Реализовать функцию, принимающую два числа 
# (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть 
# обработку ситуации деления на ноль.

def get_numbers() -> float:
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    return a, b


def get_rezult(delitel, delimoe):
    try:
        chastnoe = delitel/delimoe
        print(f'{delitel} : {delimoe} = {chastnoe}')
        main()
    except ZeroDivisionError:
        print("Делить на ноль нельзя! Попробуй еще раз..")
        main()


def main():
    delitel, delimoe = get_numbers()
    get_rezult(delitel, delimoe)


if __name__ == '__main__':
    print("Задание №1")
    main()
