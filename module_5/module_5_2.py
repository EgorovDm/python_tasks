#!/usr/bin/env python3
import module_5_1

class House(module_5_1.House):
    """House class for test task"""
    def __len__(self) -> int:
        return self.number_of_floors
    
    def __str__(self) -> str:
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

if __name__ == "__main__":
    h1 = House("ЖК Эльбрус", 10)
    h2 = House("ЖК Акация", 20)
    # __str__
    print(h1)
    print(h2)
    # __len__
    print(len(h1))  
    print(len(h2))
