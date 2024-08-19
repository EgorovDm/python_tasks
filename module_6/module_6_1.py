#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# wizardlm2:7b (no fixes)

# ai comment
# Обратите внимание, что в реальных условиях Python мог бы предложить 
# более короткие и современные подходы, например, с использованием dataclasses 
# для генерации классов или typing для строгого определения типов. 
# Но для демонстрации базовых знаний и понимания наследования, 
# представленный код является адекватным.

class Animal:
    def __init__(self, name, alive=True):
        self.alive = alive
        self.fed = False
        self.name = name

    def eat(self, food):
        if isinstance(food, Plant) and food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Plant:
    def __init__(self, name, edible=False):
        self.edible = edible
        self.name = name


class Mammal(Animal):
    # Мы не добавляем дополнительных атрибутов или методов, 
    # так как они уже наследуемы
    pass


class Predator(Mammal):
    # Также не добавляем дополнительных атрибутов или методов
    pass


class Flower(Plant):
    # Также не добавляем дополнительных атрибутов или методов
    pass


class Fruit(Plant):
    def __init__(self, name, edible=True):
        super().__init__(name, edible)

# AI check
# lion = Predator("Лев", alive=True)
# cheetah = Mammal("Гепард", alive=True)
# apple = Fruit("Яблоко", edible=True)
# poisonous_flower = Flower("Ядовитая трава", edible=False)
# 
# # Продемонстрируем работу классов
# lion.eat(apple)  # Лев съел Яблоко, теперь он насыщен
# print(f"Лев насыщен: {lion.fed}")  # Вывод: Лев насыщен: True
# 
# cheetah.eat(poisonous_flower)  # Гепард не стал есть Ядовитая трава, теперь он погибнет
# print(f"Гепард жив: {cheetah.alive}")  # Вывод: Гепард жив: False


# проверка по заданию

a1 = Predator("Волк с Уолл-Стрит")
a2 = Mammal("Хатико")
p1 = Flower("Цветик семицветик")
p2 = Fruit("Заводной апельсин")

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
