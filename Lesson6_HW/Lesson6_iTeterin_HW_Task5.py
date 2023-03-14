# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):

    def draw(self):
        print(f"Рисуем с помощью ручки {self.title}")


class Pencil(Stationery):

    def draw(self):
        print(f"Начинаем рисовать с помощью {self.title}")


class Handle(Stationery):

    def draw(self):
        print(f"Аккуратно рисуем с помощью маркера {self.title}")


def main():
    pen = Pen("шариковая ручка")
    pen.draw()

    pencil = Pencil("черный карандаш")
    pencil.draw()

    handle = Handle("зеленый маркер")
    handle.draw()


if __name__ == '__main__':
    print("Задание №1")
    main()
