# 3. Реализовать функцию my_func()
# которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.

def input_data():
    a = input("a: ")
    b = input("b: ")
    c = input("c: ")
    return a, b, c


def my_func(a, b, c):
    list_numbers = [int(a), int(b), int(c)]
    list_numbers.sort(reverse=True)
    return list_numbers[0]+list_numbers[1]

1
def main():
    a, b, c = input_data()
    print(my_func(a, b, c))


if __name__ == '__main__':
    print("Задание №3")
    main()
