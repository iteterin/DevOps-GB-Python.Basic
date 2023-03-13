# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.color} {self.name} поехала!")

    def stop(self):
        print(f"{self.color} {self.name} остановилась!")

    def turn(self, direction):
        print(f"{self.color} {self.name} повернула {direction}")

    def show_speed(self):
        print(f"Скорость {self.color} {self.name} - {self.speed} km/h")


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("Скорость превышена!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("Скорость превышена!")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


def main():
    town_car = TownCar(70, "Красная", "Toyota Prius")
    town_car.show_speed()
    town_car.turn("влево")

    work_car = WorkCar(30, "Желтый", "велосипед")
    work_car.show_speed()
    work_car.stop()

    police_car = PoliceCar(100, "Белый", "Hyundai Santa Fe")
    police_car.show_speed()

    sport_car = SportCar(180, "Заленая", "Lamborghini")
    sport_car.go()
    sport_car.show_speed()

    police_car.turn("вправо")


if __name__ == '__main__':
    print("Задание №4")
    main()
