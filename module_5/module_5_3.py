#!/usr/bin/env python3
import module_5_2

class House(module_5_2.House):
    def __int__(self) -> int:
        return self.number_of_floors
    def __eq__(self, other) -> bool:
        return self.number_of_floors == int(other)
    def __lt__(self, other) -> bool:
        return self.number_of_floors < int(other)
    def __le__(self, other) -> bool:
        return self.number_of_floors >= int(other)
    def __gt__(self, other) -> bool:
        return self.number_of_floors > int(other)
    def __ge__(self, other) -> bool:
        return self.number_of_floors >= int(other)
    def __ne__(self, other) -> bool:
        return self.number_of_floors != int(other)
    def __add__(self, value: int) -> object:
        self.number_of_floors += int(value)
        return self
    def __radd__(self, value: int) -> object:
        return self.__add__(value)
    def __iadd__(self, value: int) -> object:
        return self.__add__(value)
    # a little bit of humor
    def __invert__(self):
        self.number_of_floors *= -1
        self.name = "Бункер " + self.name
        self.sign *= -1
        return self
    def __sub__(self, value: int) -> object:
        self.number_of_floors -= int(value)
        return self
    def __truediv__(self, value: int) -> object:
        self.number_of_floors = int(self.number_of_floors/int(value))
        return self
    def __mul__(self, value: int) -> object:
        self.number_of_floors *= int(value)
        return self

if __name__ == "__main__":
    h1 = House("ЖК Эльбрус", 10)
    h2 = House("ЖК Акация", 20)
    print(h1)
    print(h2)
    print(h1 == h2)  # __eq__
    h1 = h1 + 10  # __add__
    print(h1)
    print(h1 == h2)
    h1 += 10  # __iadd__
    print(h1)
    h2 = 10 + h2  # __radd__
    print(h2)
    print(h1 > h2)  # __gt__
    print(h1 >= h2)  # __ge__
    print(h1 < h2)  # __lt__
    print(h1 <= h2)  # __le__
    print(h1 != h2)  # __ne__
    h1 = ~h1
    print(h1)
    h1.go_to(5)
    h2 *= 2
    print(h2)
    h2 /= 2
    print(h2)
