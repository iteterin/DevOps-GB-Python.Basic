# 7. Реализовать проект «Операции с комплексными числами».

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return ComplexNumber(self.real * other.real - self.imag * other.imag,
                             self.real * other.imag + self.imag * other.real)

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"


def main():
    # создаем комплексные числа
    num1 = ComplexNumber(2, 3)  # 2+3i
    num2 = ComplexNumber(-1, 2)  # -1+2i

    # выполняем операции
    sum_res = num1 + num2  
    mul_res = num1 * num2

    # выводим результаты
    print(f"Сумма: {sum_res}")
    print(f"Произведение: {mul_res}")

if __name__ == '__main__':
    print("Задание №7")
    main()

"""
(2+3i) + (-1+2i) = (2 + (-1)) + (3 + 2)·i = 1+5i
(2+3i) * (-1+2i) = (2*(-1) - 3*2) + (3*(-1) + 2*2)*i = -8+i
"""