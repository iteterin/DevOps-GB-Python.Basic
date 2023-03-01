# 2. Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.

def input_data() -> dict:
    input_dict = dict()
    input_dict["Имя"] = input("Введите имя пользователя: ")
    input_dict["Фамилия"] = input("Введите фамилию пользователя: ")
    input_dict["Год рождения"] = input("Введите год рождения пользователя: ")
    input_dict["Город проживания"] = input(
        "Введите город проживания пользователя: ")
    input_dict["email"] = input("Введите электронную почту пользователя: ")
    input_dict["Телефон"] = input("Введите телефон пользователя: ")
    return input_dict


def print_user_data(Name, Surname, Born, City, Email, Phone):
    print(f'{Name} {Surname} {Born} {City} {Email} {Phone}')


def main():
    user_data = input_data()
    print_user_data(Name=user_data["Имя"], Surname=user_data["Фамилия"], Born=user_data["Год рождения"],
                    City=user_data["Город проживания"], Email=user_data["email"], Phone=user_data["Телефон"])


if __name__ == '__main__':
    print("Задание №2")
    main()
