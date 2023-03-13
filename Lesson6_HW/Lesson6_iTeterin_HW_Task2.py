# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу:
# длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, 
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_asphalt_mass(self, mass_of_asphalt_to_cover_1_sq_meters=25, thickness_of_canvas=5):
        asphalt_mass = self._length * self._width * mass_of_asphalt_to_cover_1_sq_meters * thickness_of_canvas / 1000
        return asphalt_mass


def main():
    road = Road(20, 5000)
    asphalt_mass = road.calculate_asphalt_mass()
    print(f'Масса асфальта для покрытия всей дороги: {asphalt_mass} тонн.')


if __name__ == '__main__':
    print("Задание №1")
    main()
