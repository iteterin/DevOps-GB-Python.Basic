# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты:
# name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного
# имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


def main():
    employee1 = Position('Иван', 'Иванов', 'менеджер', 30000, 0)
    print(f'Сотрудник: {employee1.get_full_name()}')
    print(f'Доход с учётом премии: {employee1.get_total_income()} руб.')

    employee2 = Position('Петр', 'Петров', 'инженер', 20000, 10000)
    print(f'Сотрудник: {employee2.get_full_name()}')
    print(f'Доход с учётом премии: {employee2.get_total_income()} руб.')


if __name__ == '__main__':
    print("Задание №1")
    main()
