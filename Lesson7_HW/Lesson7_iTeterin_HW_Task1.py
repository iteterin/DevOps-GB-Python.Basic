# Реализовать класс Matrix (матрица). Обеспечить перегрузку
#   конструктора класса (метод __init__()), который должен
#   принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин,
#   расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__()
#   для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()
#   для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять
#   поэлементно — первый элемент первой строки первой матрицы
#   складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += "\t".join(str(val) for val in row) + "\n"
        return matrix_str

    def __add__(self, other):
        #Для сложения матриц их размерность должна совпадать. Проверяем, предупреждаем. 
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Матрицы должны иметь одинаковый размер")

        result = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[0])):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)

        return Matrix(result)


def main():
    # Создание матрицы1 3x3
    m1 = Matrix([[1, 2], [3, 4],[5, 6]])

    # Создание матрицы1 3x3
    m2 = Matrix([[5, 6], [7, 8], [9, 10]])

    # Вывод матрицы в виде строки
    print(m1)

    # Сложение матриц
    result_3_3 = m1 + m2
    print(result_3_3)

    # Создание матрицы1 2x4
    m4 = Matrix([[1, 1, 1, 1], [9, 9, 9, 9]])

    # Создание матрицы1 2x4
    m5 = Matrix([[9, 9, 9, 9], [1, 1, 1, 1]])

    # Сложение матриц
    result_2_4 = m4 + m5
    print(result_2_4)

if __name__ == '__main__':
    print("Задание №1")
    main()
