#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# wizardlm2:7b + fix

def add_everything_up(a, b):
    # Проверяем, являются ли оба аргумента одного и того же типа
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        # complience with task desierd output, float has final precision
        # ~ 16 decimal digits (53 bit), 12 digits precision removes all artifacts
        return round(a + b, 12)
    else:
        return f"{a}{b}"


# Примеры использования функции
print(add_everything_up(123.456, "строка"))  # '123.456строка'
print(add_everything_up("яблоко", 4215))  # 'яблоко4215'
print(add_everything_up(123.456, 7))  # 130.456
# proof of float precision problem
# print(add_everything_up(123.4560001, 7))
