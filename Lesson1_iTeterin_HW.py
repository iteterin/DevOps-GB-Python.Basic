#1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
print("Задание №1")
переменная_1 = "Какой-то текст"
переменная_2 = 1992
переменная_3 = int(input("Введите день своего рождения: "))
переменная_4 = (input("Введите название месяца своего рождения: "))

print(f" Содержимое переменной 1: {переменная_1}")
print(f" Содержимое переменной 2: {переменная_2}")
print(f" Содержимое переменной 3: {переменная_3}")
print(f" Содержимое переменной 4: {переменная_4}")

#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
print("Задание №2")
время_от_пользователя = int(input("Введите время в секундах: "))
часов = время_от_пользователя // 3600
минут = время_от_пользователя // 60 - часов * 60
секунд = время_от_пользователя % 60
print(f"{часов:02}:{минут:02}:{секунд:02}")

#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
print("Задание №3")
число_n = input("Введите число n: ")

while число_n < '0':
    print("Нужно ввести число больше нуля!Попробуй еще раз..")
    число_n = input("Введите число n: ")

print(f"{число_n} + {число_n + число_n} + {число_n + число_n + число_n } = {int(число_n) + int(число_n + число_n) + int(число_n + число_n + число_n)}")

#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
print("Задание №4")
число = int(input("Введите целое положительное число: "))
текущий_максимум = 0
остаток = число

while остаток > 0:
    последняя_цифра = число % 10
    if последняя_цифра > текущий_максимум:
        текущий_максимум = последняя_цифра
        if текущий_максимум == 9:
            break
    остаток = остаток // 10

print(f"Наибольшая цифра в числе {число} - {текущий_максимум}")


#5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
print("Задание №5")
Выручка = float(input("Введите выручку (руб): "))
Издержки = float(input("Введите издержки (руб): "))
Результат = Выручка - Издержки
if Результат > 0:
    print(f"Компания работает с прибылью {Результат}")
    print(f"Рентабельность выручки: {100 * Результат / Выручка:.1f}%")
    КолВо_Сотрудников = int(input("Введите кол-во сотрудников: "))
    print(f"Если разделить прибыль по ровну, то каждый получит: {Результат/КолВо_Сотрудников:.3f} руб.")
elif Результат < 0:
    print(f"Компания работает в убыток: {-Результат}")
else:
    print("Ни рыба, ни мясо - работаем в 0!")

#6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который результат спортсмена составит не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
#Например: a = 2, b = 3.
#Результат:
#1-й день: 2
#2-й день: 2,2
#3-й день: 2,42
#4-й день: 2,66
#5-й день: 2,93
#6-й день: 3,22
#
#Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

print("Задание №6")
firstday_km = int(input("Введите результат спортсмена в первый день: "))
rezultat_km = int(input("Введите результат, который спорцмен должен достигнуть: "))
seychas_km = firstday_km
day = 1

print(f"{day}-ый день: {seychas_km}")
while seychas_km <= rezultat_km:
    day += 1
    seychas_km = seychas_km + ((seychas_km / 100) *10)
    print(f"{day}-ый день: {seychas_km}")
print(f"Ответ: на {day}-й день спортсмен достигнет результата - не менее {rezultat_km} км.")