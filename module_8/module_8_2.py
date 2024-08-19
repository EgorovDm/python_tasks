#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# wizardlm2:7b + 2 fixes

import traceback

def personal_sum(numbers):
    incorrect_data = 0
    total = sum(number for number in numbers if isinstance(number, (int, float)))
    for number in numbers:
        if not isinstance(number, (int, float)):
            try:
                # Intentionally causing TypeError to handle it
                total += number
            except TypeError:
                incorrect_data += 1
                print(f"Некорректный тип данных для подсчёта суммы - {number}")
    return total, incorrect_data

def calculate_average(numbers):
    try:
        result, count = personal_sum(numbers)
        count = len(numbers) - count
        if count == 0:
            print("Коллекция пуста.")
        return result / count
    except TypeError:
        print("В numbers записан некорректный тип данных")
        return None
    except ZeroDivisionError:
        return 0
print(
    f'Результат 1: {calculate_average("1, 2, 3")}\n'
)  # Строка перебирается, но каждый символ - строковый тип

print(
    f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}\n'
)  # Учитываются только 1 и 3

print(f"Результат 3: {calculate_average(567)}\n")  # Передана не коллекция
print(f"Результат 4: {calculate_average([42, 15, 36, 13])}\n")  # Всё должно работать