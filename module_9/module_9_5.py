#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# wizardlm2:7b + 2 fixes

# Класс исключения StepValueError, наследуемый от ValueError
class StepValueError(ValueError):
    pass

# Класс Iterator
class Iterator:
    def __init__(self, start, stop, step=1):
        if step == 0:
            raise StepValueError("шаг не может быть равен 0")
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start - step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            # Если шаг положительный, увеличиваем покатор до тех пор, пока не станет больше stop
            if self.pointer < self.stop:
                self.pointer += self.step
            else:
                raise StopIteration
        else:
            # Если шаг отрицательный, уменьшаем покатор до тех пор, пока не станет меньше stop
            if self.pointer > self.stop:
                self.pointer += self.step
            else:
                raise StopIteration
        return self.pointer


# Пример выполняемого кода
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=" ")
except StepValueError as e:
    print(e)

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=" ")
print()

for i in iter3:
    print(i, end=" ")
print()

for i in iter4:
    print(i, end=" ")
print()

for i in iter5:
    print(i, end=" ")
print()
