#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Horse:
    def __init__(self):
        self.x_distance = 0
        self.sound='Frrr'
        
    def run(self, dx):
        self.x_distance += dx
        
    def voice(self):
        print(self.sound)

class Eagle:
    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'
        
    def fly(self, dy):
        self.y_distance += dy
        
    def voice(self):
        print(self.sound)

class Pegasus(Horse, Eagle):
    def __init__(self):
        #manual fix
        super(Pegasus, self).__init__() # Указано для корректного вызова конструктора родителя
        
    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)
        
    def get_pos(self):
        return (self.x_distance, self.y_distance)
    
    def voice(self):
        super().voice()  # Печать звука от Horse
        super(Eagle, self).voice()  # Печать звука от Eagle


p1 = Pegasus()

print(p1.get_pos())  # Вывод: (0, 0)
p1.move(10, 15)
print(p1.get_pos())  # Вывод: (10, 15)
p1.move(-5, 20)
print(p1.get_pos())  # Вывод: (5, 35)

p1.voice()  # Выход звука 'I train, eat, sleep, and repeat'

