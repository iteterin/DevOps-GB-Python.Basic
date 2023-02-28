#-------------------------------------------------------------------------------------------------------------------------------
"""
1. Создать список и заполнить его элементами различных типов данных. 
Реализовать скрипт проверки типа данных каждого элемента. 
Использовать функцию type() для проверки типа. 
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""
#-------------------------------------------------------------------------------------------------------------------------------
import sys

def input_data():
    print("Введите данные разных типов через пробел (например: Сестра помыла 1.5 окна. Сестре 20 лет. )")
    line = sys.stdin.readline().rstrip()
    line_data = list()

    for i in line.split():
        try:
            temp_data = int(i)
        except ValueError:
            try :
                temp_data = float(i)
            except ValueError:
                temp_data = str(i)
        line_data.append(temp_data)

    return line_data

def get_type(list_data): 
    print (f"Список: {list_data}")
    for i in list_data:
        print (f"Элемент строки: {i}, имеет тип: {type(i)}")


def main():
    data = input_data()
    get_type(data)

if __name__ == '__main__':
    print("Задание №1")
    main()
#-------------------------------------------------------------------------------------------------------------------------------
"""
2. Для списка реализовать обмен значений соседних элементов. 
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д. 
При нечётном количестве элементов последний сохранить на своём месте. 
Для заполнения списка элементов нужно использовать функцию input().
"""
#-------------------------------------------------------------------------------------------------------------------------------
import sys

def input_data():
    line = sys.stdin.readline().rstrip()
    list_data = [str(x) for x in line.split()]
    num_list = len(list_data)
    return num_list, list_data

def set_list_value(len_list, data_list)-> list():
    print(f"Исходный список: {data_list}, кол-во этементов: {len_list}")
    if (len_list %2 != 0):
        len_list = len_list - 1
    
    for i in range(0,len_list):
        if (i %2 ==0):
            temp_i = data_list[i] 
            data_list[i] = data_list[i+1]
            data_list[i+1] = temp_i

    print(f"Измененный список: {data_list}")
    

def main():
    n, data = input_data()
    set_list_value(n, data)

if __name__ == '__main__':
    print("Задание №2")
    main()
#входные данные:
#1 кошка 45 вода 1703
#1 кошка 45 вода 1703 2023
#-------------------------------------------------------------------------------------------------------------------------------
"""
3. Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). 
Напишите решения через list и dict.
"""
#-------------------------------------------------------------------------------------------------------------------------------
def input_data():
    user_input = ''
    while user_input is not int:
        try:
            user_input = int(input("Введите число от 1 до 12: "))
            if 1 <= user_input <= 12:
                break
            else:
                print(f'Вы ввели число {user_input}! Введите число в диапазоне от 1 до 12.')
        except ValueError:
            print('Вы ввели не число или оно не целое! Введите число в диапазоне от 1 до 12.')
    return user_input

def month_from_list(number)-> str:
    month_list = ["Январь","Февраль","Март","Апрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь"]
    print(f"Список. Выбран месяц: {number} - это месяц {month_list[number-1]}")

def month_from_dict(number):
    month_dictionary = {1:"Январь", 2:"Февраль", 3:"Март", 4:"Апрель", 5:"Май", 6:"Июнь", 7:"Июль", 8:"Август", 9:"Сентябрь", 10:"Октябрь", 11:"Ноябрь", 12:"Декабрь"}
    print(f"Словарь. Выбран месяц: {number} - это месяц {month_dictionary[number]}")

def main():
    number_month = input_data()
    month_from_list(number_month)
    month_from_dict(number_month)

if __name__ == '__main__':
    print("Задание №3")
    main()
#-------------------------------------------------------------------------------------------------------------------------------
"""
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. 
Вывести каждое слово с новой строки. 
Строки нужно пронумеровать. 
Если слово длинное, выводить только первые 10 букв в слове.
"""
#-------------------------------------------------------------------------------------------------------------------------------
import sys

def input_data():
    line = sys.stdin.readline().rstrip()
    line = [str(x) for x in line.split()]
    return line

def main():
    data_list = input_data()
    n = len(data_list)
    j = 1
    for i in range(n):
        if len(data_list[i]) >= 10:
            data_list[i] = (data_list[i])[0:10]
        print(f"{j} {data_list[i]}")
        j+=1

if __name__ == '__main__':
    print("Задание №4")
    main()
#Входные данные:Реализовать структуру данных «Товары» Она должна представлять собой список кортежей
#-------------------------------------------------------------------------------------------------------------------------------
"""
5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
 У пользователя нужно запрашивать новый элемент рейтинга. 
 Если в рейтинге существуют элементы с одинаковыми значениями, 
 то новый элемент с тем же значением должен разместиться после них.

Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].
"""
#-------------------------------------------------------------------------------------------------------------------------------
import sys

def input_new_raiting(raiting_data):
    trigger = True
    new_raitnig_value = ''
    insert_in_the_end = False
    while trigger: 
        try:
            user_input = input("Введите новый рейтинг или 's' что бы остановить работу программы: ")
            if user_input == "s":
                trigger = False
            else:
                user_input = int(user_input)
                new_raitnig_value = user_input
        except ValueError:
            print('Вы ввели не число или оно не целое! Введите натуральное число!')
        #Можно пихнуть значение в конец и отсортировать по убыванию, никто не узнает... :) Но это было бы читерством
        try:
            raiting_data.insert(raiting_data.index(new_raitnig_value),new_raitnig_value)
        except ValueError:
            for i in range(0,len(raiting_data)):
                if new_raitnig_value > raiting_data[i]:
                    raiting_data.insert(i, new_raitnig_value)
                    insert_in_the_end = False
                    break
                else:
                    insert_in_the_end = True
            if insert_in_the_end:
                raiting_data.insert(len(raiting_data)+1, new_raitnig_value)
        print(f'Текущий рейтинг: {raiting_data}')
    print(f'Итоговый рейтинг: {raiting_data}')

def input_data()->list:
    print("Введите несколько чисел, разделенных пробелом для заполнения списка рейтинга (например: 7 5 3 3 2):")
    line = sys.stdin.readline().rstrip()
    raiting = [int(x) for x in line.split()]
    raiting.sort(reverse=True)
    return raiting

def main():
    raiting = input_data()
    input_new_raiting(raiting)

if __name__ == '__main__':
    print("Задание №5")
    main()

#Входные данные: 1 10 10 3 4 5 6 6 7 8 9 11 14
#-------------------------------------------------------------------------------------------------------------------------------
"""
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. 
Каждый кортеж хранит информацию об отдельном товаре. 
В кортеже должно быть два элемента — номер товара и словарь с параметрами, 
то есть характеристиками товара: 
название, цена, количество, единица измерения. 
Структуру нужно сформировать программно, запросив все данные у пользователя.

Пример готовой структуры:

[
(1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
(2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
(3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]

Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например, название. Тогда значение — список значений-характеристик, например, список названий товаров.
Пример:

{
“название”: [“компьютер”, “принтер”, “сканер”],
“цена”: [20000, 6000, 2000],
“количество”: [5, 2, 7],
“ед”: [“шт.”]
}
"""
#-------------------------------------------------------------------------------------------------------------------------------
def input_item_data()->dict:
    item_name = input("Введите название: ")
    item_cost = int(input("Введите цену: "))
    item_count = int(input("Введите кол-во: "))
    item_value = input("Введите единицу (шт., литры, кг и т.д.): ")
    item = {"Название":item_name, "Цена":item_cost, "Колличество":item_count, "Единица": item_value}
    return item

def create_structure()->list():
    i = 1
    data_list = list()
    while True:
        continue_var = input("Добавить данные в структуру? [y/n]: ")
        if continue_var == 'n':
            break
        elif continue_var == 'y':
            data_item = input_item_data()
            item_list = [i, data_item]
            item_tuple = tuple(item_list)
            data_list.append(item_tuple)
            i+=1
            del item_list, item_tuple,data_item
        else:
            print("Вы ввели не правильные данные. Введите только y или n. Попробуйте еще раз..")
    return data_list

def get_analytic(struct)->dict:

    items_names = list()
    items_costs = list()
    items_counts = list()
    items_values = list()

    for i in range(0,len(struct)):
        items_names.append(struct[i][1].get("Название"))
        items_costs.append(struct[i][1].get("Цена"))
        items_counts.append(struct[i][1].get("Колличество"))
        items_values.append(struct[i][1].get("Единица"))
    
    items_names = list(set(items_names))
    items_costs = list(set(items_costs))
    items_counts = list(set(items_counts))
    items_values = list(set(items_values))

    analytic = {"Название":items_names, "Цена":items_costs, "Колличество":items_counts, "Единица":items_values}
    return analytic

def main():
    print("Постоение структуры..")
    structure = create_structure()
    print("Структура:")
    print(structure)
    print("Аналитика:")
    analytic = get_analytic(structure)
    print(analytic)

if __name__ == '__main__':
    print("Задание №6")
    main()
#-------------------------------------------------------------------------------------------------------------------------------