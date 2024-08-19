#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# wizardlm2:7b (2 fixes)

from typing import List

class Vehicle:
    __COLOR_VARIANTS: List[str] = ['red', 'blue', 'black', 'white', 'green']  # Список допустимых цветов

    def __init__(self, owner: str, model: str, color: str, engine_power: int):
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color if color.lower() in Vehicle.__COLOR_VARIANTS else None
        self.owner = owner

    def get_model(self) -> str:
        return f"Модель: {self.__model}"

    def get_horsepower(self) -> str:
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self) -> str:
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str):
        if new_color.lower() in Vehicle.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}.")

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner: str, model: str, engine_power: int, color: str, passengers_limit=__PASSENGERS_LIMIT):
        super().__init__(owner, model, engine_power, color)
        self.__passengers_limit = passengers_limit

    def get_passengers_limit(self) -> str:
        return f"Лимит пассажиров: {self.__passengers_limit}"


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan("Fedos", "Toyota Mark II", "blue", 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color("Pink")
vehicle1.set_color("BLACK")     
vehicle1.owner = "Vasyok"

# Проверяем что поменялось
vehicle1.print_info()


