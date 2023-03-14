# 3. Создайте собственный класс-исключение,
# который должен проверять содержимое списка на наличие только чисел.
# Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.


class NotANumberError(Exception):
    pass


def main():
    number_list = []

    while True:
        try:
            user_input = input("Введите число (stop для завершения): ")
            if user_input == 'stop':
                break
            elif not user_input.isdigit():
                raise NotANumberError("Введено не число")
            else:
                number_list.append(int(user_input))
        except NotANumberError as err:
            print(err)

    print("Список чисел: ", number_list)


if __name__ == '__main__':
    print("Задание №3")
    main()
