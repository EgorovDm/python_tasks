#!/usr/bin/env python3
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if isinstance(new_floor, int):  # Проверяем, что new_floor - целое число
            if 1 <= new_floor <= self.number_of_floors:
                for floor in range(1, new_floor + 1):
                    print(floor)
            else:
                print("Такого этажа не существует")
        else:
            raise ValueError("Номер этажа должен быть целым числом")

# Пример использования класса с проверкой типа:
try:
    my_house = House('ЖК Эльбрус', 30)
    my_house.go_to(15)  # Выведет числа от 1 до 15 включительно
    h1 = House('ЖК Горский', 18)
    h2 = House('Домик в деревне', 2)
    h1.go_to(5)
    h2.go_to(10)
except ValueError as e:
    print(e)
