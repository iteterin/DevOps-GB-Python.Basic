# 4,5,6 Создайте класс, описывающий склад. А также класс «Оргтехника»...

class Storage:
    def __init__(self):
        self.inventory = {}
    
    def add_item(self, item_type, item_name, item_count, item_features):
        if not isinstance(item_count, int):
            raise ValueError("Ошибка: количество должно быть целым числом")
        if item_count <= 0:
            raise ValueError("Количество должно быть больше нуля.")
        if item_type not in self.inventory:
            self.inventory[item_type] = {}
        if item_name not in self.inventory[item_type]:
            self.inventory[item_type][item_name] = {'count': 0, 'features': item_features}
        self.inventory[item_type][item_name]['count'] += item_count
    
    def remove_item(self, item_type, item_name, item_count, dest_department):
        if not isinstance(item_count, int):
            raise ValueError("Ошибка: количество должно быть целым числом")
        if item_type not in self.inventory:
            raise ValueError("Ошибка: на складе нет такого типа техники")
        if item_name not in self.inventory[item_type]:
            raise ValueError("Ошибка: на складе нет такого оборудования")
        if self.inventory[item_type][item_name]['count'] < item_count:
            raise ValueError("Ошибка: на складе недостаточно оборудования")
        if dest_department not in self.inventory:
            self.inventory[dest_department] = {}
        if item_name not in self.inventory[dest_department]:
            self.inventory[dest_department][item_name] = {'count': 0, 'features': self.inventory[item_type][item_name]['features']}
        self.inventory[item_type][item_name]['count'] -= item_count
        self.inventory[dest_department][item_name]['count'] += item_count
    
    def inventory_check(self):
        print("Инвентаризация склада:")
        for item_type, item_names in self.inventory.items():
            print(f"Тип техники: {item_type}")
            for item_name, item_info in item_names.items():
                print(f"\t{item_name}: {item_info['count']} шт. {item_info['features']}")


class OfficeEquipment:
    def __init__(self, name, features):
        self.name = name
        self.features = features


class Printer(OfficeEquipment):
    def __init__(self, name, features, color):
        super().__init__(name, features)
        self.color = color


class Scanner(OfficeEquipment):
    def __init__(self, name, features, resolution):
        super().__init__(name, features)
        self.resolution = resolution


class Xerox(OfficeEquipment):
    def __init__(self, name, features, two_sided_printing):
        super().__init__(name, features)
        self.two_sided_printing = two_sided_printing



def main():

    # создаем объекты оборудования и склад
    printer1 = Printer("Принтер HP", "лазерный", True)
    printer2 = Printer("Принтер Canon", "струйный", False)
    scanner1 = Scanner("Сканер Epson", "планшетный", "1200x1200 dpi")
    scanner2 = Scanner("Сканер Brother", "книжный", "600x600 dpi")
    xerox1 = Xerox("Ксерокс Xerox", "лазерный", True)
    xerox2 = Xerox("Ксерокс Samsung", "лазерный", False)
    warehouse = Storage()

    # добавляем оборудование на склад
    try:
        warehouse.add_item('принтеры', printer1.name, 10, printer1.color)
    except Exception as e:
        print(e)
    try:   
        warehouse.add_item('принтеры', printer2.name, -5, printer2.color)
    except Exception as e:
        print(e)
    try:    
        warehouse.add_item('сканеры', scanner1.name, 3, scanner1.resolution)
    except Exception as e:
        print(e)
    try:
        warehouse.add_item('сканеры', scanner2.name, 7, scanner2.resolution)
    except Exception as e:
        print(e)
    try:
        warehouse.add_item('ксероксы', xerox1.name, 2, xerox1.two_sided_printing)
    except Exception as e:
        print(e)
    try:
        warehouse.add_item('ксероксы', xerox2.name, 1, xerox2.two_sided_printing)
    except Exception as e:
        print(e)
    
    # выводим текущее состояние склада
    warehouse.inventory_check()

    # перемещаем оборудование из склада в отдел компании
    try:
        warehouse.remove_item('принтеры', printer1.name, 30, 'Отдел продаж')
    except Exception as e:
        print(e)
    try:
        warehouse.remove_item('сканеры', scanner2.name, 2, 'Бухгалтерия')
    except Exception as e:
        print(e)
    # выводим текущее состояние склада после перемещения оборудования
    warehouse.inventory_check()


if __name__ == '__main__':
    print("Задание №4")
    main()





