#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# wizardlm2:7b (3 fixes)

class Horse:
    def __init__(self):
        super(Horse, self).__init__()
        self.x_distance = 0
        self.sound = "Frrr"

    def run(self, dx):
        self.x_distance += dx


class Eagle:
    def __init__(self):
        super(Eagle, self).__init__()
        self.y_distance = 0
        self.sound = "I train, eat, sleep, and repeat"

    def fly(self, dy):
        self.y_distance += dy


class Pegasus(Eagle, Horse):
    def __init__(self):
        super(Pegasus, self).__init__()  # Инициализируем родительские классы

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


# Создание объекта класса Pegasus и вызов методов для проверки работы программы
p1 = Pegasus()
print(p1.get_pos())  # Вывод: (0, 0)

p1.move(10, 15)
print(p1.get_pos())  # Вывод: (10, 15)

p1.move(-5, 20)
print(p1.get_pos())  # Вывод: (5, 35)

p1.voice()  # Вывод: I train, eat, sleep, and repeat
