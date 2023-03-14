# 3. Реализовать программу работы с органическими клетками,
#     состоящими из ячеек.
# Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр,
#     соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки
#     арифметических операторов: сложение (__add__()),
#     вычитание (__sub__()), умножение (__mul__()),
#     деление (__truediv__()).
# Данные методы должны применяться только к клеткам
#     и выполнять увеличение, уменьшение, умножение и
#     целочисленное (с округлением до целого) деление
#     клеток, соответственно.
# В классе необходимо реализовать метод make_order(),
#     принимающий экземпляр класса и количество ячеек
#     в ряду.
# Метод должен возвращать строку вида *****\n*****\n*****...,
#     где количество ячеек между \n равно переданному
#     аргументу.


class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells - other.cells > 0:
            return Cell(self.cells - other.cells)
        else:
            print("Разность количества ячеек двух клеток меньше или равна нулю")

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, row_len=5):
        rows = self.cells // row_len
        last_row = self.cells % row_len
        return ('*' * row_len + '\n') * rows + '*' * last_row


def main():

    cell1 = Cell(10)
    cell2 = Cell(6)
    cell3 = Cell(16)

    print((cell1 + cell2).cells)  # 16
    print((cell1 - cell2).cells)  # 4
    print((cell1 * cell2).cells)  # 60
    print((cell1 / cell2).cells)  # 1

    print(cell3.make_order())


if __name__ == '__main__':
    print("Задание №3")
    main()
