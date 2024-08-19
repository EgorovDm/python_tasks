#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# wizardlm2:7b failed to falow through provided instructions
# but it was easy to fix manualy

first = ["Strings", "Student", "Computers"]
second = ["Строка", "Урбан", "Компьютер"]

# first_result - генераторная сборка, которая высчитывает разницу в длинах строк из списков first и second
first_result = (
    len(i) - len(j) for i, j in zip(first, second)
    if len(i)!= len(j)
)

# second_result - генераторная сборка, которая содержит результаты сравнения длин строк в одинаковых позициях из sписков first и second
second_result = (
    len(first[i]) == len(second[i]) for i in range(len(first))
)

# Вывод результатов
print(list(first_result))
print(list(second_result))
