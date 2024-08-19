#!/usr/bin/env python3

class House:
    """House class for test task"""
    def __init__(self, name: str, number_of_floors: int) -> None:
        self.name = name
        self.number_of_floors = number_of_floors
        # for 3d task
        self.sign = int(number_of_floors / abs(number_of_floors))

    def go_to(self, new_floor: int) -> None:
        if abs(self.number_of_floors) > new_floor > 0:
            # implementation for 3d task
            [print(i * self.sign) for i in range(1, abs(new_floor) + 1)]
        else:
            print("\"Такого этажа не существует\"")

if __name__ == "__main__":
    h1 = House("ЖК Горский", 18)
    h2 = House("Домик в деревне", 2)
    h1.go_to(5)
    h2.go_to(10)
