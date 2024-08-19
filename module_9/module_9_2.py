#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# wizardlm2:7b + 1 fix

import itertools

first_strings = ["Elon", "Musk", "Programmer", "Monitors", "Variable"]
second_strings = ["Task", "Git", "Comprehension", "Java", "Computer", "Assembler"]

# first_result - список длин строк, где длина строки не менее 5 символов
first_result = [len(s) for s in first_strings if len(s) >= 5]

# second_result - список кортежей, где каждый элемент - пара слов одинаковой длины из first и second strings
# Roughly equivalent to nested for-loops ~ ((x,y) for x in A for y in B)
pairwise = itertools.product(first_strings, second_strings)
second_result = [pair for pair in pairwise if len(pair[0]) == len(pair[1])]

# third_result - словарь, где ключом является строка, а значением - длина этой строки
third_result = {
    s: len(s)
    for s in set(first_strings + second_strings)
    if len(s) % 2 == 0
}

# Вывод результатов
print(first_result)
print(second_result)
print(third_result)
