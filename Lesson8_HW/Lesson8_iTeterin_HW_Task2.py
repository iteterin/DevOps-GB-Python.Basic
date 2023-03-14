# 2. Создайте собственный класс-исключение, обрабатывающий
#    ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно
#    обработать эту ситуацию и не завершиться с ошибкой.


class DivisionByZeroError(Exception):
    pass


def main():
    try:
        dividend = int(input("Введите делимое: "))
        divisor = int(input("Введите делитель: "))
        if divisor == 0:
            raise DivisionByZeroError("Деление на ноль невозможно!")
        quotient = dividend / divisor
        print("Частное: ", quotient)
    except ValueError:
        print("Пожалуйста, введите только целочисленные значения")
    except DivisionByZeroError as err:
        print(err)
    except Exception as err:
        print("Произошла ошибка:", err)


if __name__ == '__main__':
    print("Задание №2")
    main()
