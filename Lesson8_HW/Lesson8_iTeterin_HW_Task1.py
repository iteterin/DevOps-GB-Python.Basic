# 1. Реализовать класс «Дата», функция-конструктор которого должна
#    принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип
#    к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию
#    числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def extract_date(cls, date_str):
        day, month, year = map(int, date_str.split("-"))
        return [day, month, year]

    @staticmethod
    def is_valid(date_str):
        day, month, year = map(int, date_str.split("-"))
        if month > 12 or month < 1:
            return False
        if day < 1:
            return False
        if month == 2:
            if year % 4 == 0:
                if day > 29:
                    return False
            else:
                if day > 28:
                    return False
        elif month in [4, 6, 9, 11]:
            if day > 30:
                return False
        else:
            if day > 31:
                return False
        return True


def main():
    date_str = "29-02-2022"  # некорректная дата
    if Date.is_valid(date_str):
        date = Date.extract_date(date_str)
        print(date)
    else:
        print("Некорректная дата")

    date_str = "31-04-2022" # некорректная дата
    if Date.is_valid(date_str):
        date = Date.extract_date(date_str)
        print(date)
    else:
        print("Некорректная дата") 

    date_str = "31-05-2022"  # корректная дата
    if Date.is_valid(date_str):
        date = Date.extract_date(date_str)
        print(date)
    else:
        print("Некорректная дата")


if __name__ == '__main__':
    print("Задание №1")
    main()
