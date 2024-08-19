#!/usr/bin/env python3
import module_5_3

class House(module_5_3.House):
    """House class for test task"""
    houses_history = []
    house_in_use = []
    def __new__(cls, *args, **kwargs):
        if (args[0] or kwargs["name"]) in cls.house_in_use:
            raise ValueError("Дом уже существует!")
        else:
            cls.houses_history.append(args[0] or kwargs["name"])
            cls.house_in_use.append(args[0] or kwargs["name"])
        return super().__new__(cls)
    def __del__(self):
        self.house_in_use.remove(self.name)
        print(f"{self.name} снесён, но он останется в истории")

if __name__ == "__main__":
    h1 = House("ЖК Эльбрус", 10)
    print(House.houses_history)
    h2 = House("ЖК Акация", 20)
    print(House.houses_history)
    h3 = House("ЖК Матрёшки", 20)
    print(House.houses_history)
    # print(House.house_in_use)
    # Удаление объектов
    del h2
    del h3
    # print(House.house_in_use)
    print(House.houses_history)
    print('Exiting...')
    exit(0)
