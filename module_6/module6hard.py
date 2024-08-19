#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# wizardlm2:7b (+ fixes)

class Figure:
    def __init__(self, color, sides):
        self.__color = color
        self.__sides = sides
        self.__height = 0

    def set_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                self.__color = (r, g, b)
        # Если цвета некорректны, не изменяем

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *new_sides):
        if all(
            isinstance(side, int) and side > 0 for side in new_sides
            ):
            return (len(new_sides) == 1) or (len(new_sides) == len(self.__sides))
        return False

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides[:]
        # Если стороны некорректны или количество не соответствует sides_count, не изменяем

    def get_sides(self):
        return self.__sides
    
    def get_height(self):
        return self.__height

    def set_height(self, new_height):
        if isinstance(new_height, int) and 0 < new_height:
            self.__height = new_height

    def __len__(self):
        return sum(self.__sides)

    def get_square(self):
        if self.__sides is None:
            raise NotImplementedError("get_square not implemented for Figure")
        return super().get_square(*self.__sides)

    def get_volume(self):
        if self.__sides is None and isinstance(self.__sides, (int, float)):
            return super().get_volume(self.__sides)
        else:
            raise NotImplementedError("get_volume not implemented for Figure")

class Circle(Figure):
    def __init__(self, color, side):
        if isinstance(side, int) and side > 0:
            super(Circle, self).__init__(color, side)
            self.__radius = side / (2 * 3.1415926535)
        else:
            raise ValueError("Incorrect side value")

    def get_radius(self):
        return self.__radius

    def get_square(self):
        return 3.1415926535 * self.get_radius() **2

    def get_perimeter(self):
        return self.__sides

class Triangle(Figure):
    SIDES_COUNT = 3

    def __init__(self, color, sides):
        super(Triangle, self).__init__(
            color,
            [sides] * self.SIDES_COUNT if len(sides) != self.SIDES_COUNT else sides,
        )
        # Предполагаем, что это прямоугольный треугольник
        self.set_height(min(sides))  

    def get_square(self):
        return 0.5 * self.get_sides()[0] * self.get_height()

class Cube(Figure):
    SIDES_COUNT = 12

    def __init__(self, color, side):
        super(Cube, self).__init__(color, [side] * self.SIDES_COUNT)

    def get_volume(self):
        return self.get_sides()[0] ** 3
    
    def get_square(self):
        return self.get_sides()[0] ** 2

    def get_surface(self):
        return self.get_square() * 6

    def set_sides(self, *new_sides):
        if set(new_sides) == 1:
            super().set_sides(*new_sides)

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())

cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
