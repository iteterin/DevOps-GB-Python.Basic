# Реализовать проект расчёта суммарного расхода ткани
#     на производство одежды. Основная сущность (класс)
#     этого проекта — одежда, которая может иметь определённое
#     название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто)
#     и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды
#     использовать формулы: для пальто (V/6.5 + 0.5),
#     для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
#     реализовать абстрактные классы для основных классов проекта,
#     проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def fabric_consumption(self):
        pass

    @property
    @abstractmethod
    def full_description(self):
        pass


class Coat(Clothes):
    def fabric_consumption(self):
        return self.param / 6.5 + 0.5

    @property
    def full_description(self):
        return f"Пальто, размер: {self.param}"


class Suit(Clothes):
    def fabric_consumption(self):
        return self.param * 2 + 0.3

    @property
    def full_description(self):
        return f"Костюм, рост: {self.param}"


def main():
    coat = Coat(50)
    print(coat.full_description)
    print(f"Расход ткани для пальто: {coat.fabric_consumption()}")

    suit = Suit(175)
    print(suit.full_description)
    print(f"Расход ткани для костюма: {suit.fabric_consumption()}")


if __name__ == '__main__':
    print("Задание №2")
    main()
