#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# wizardlm2:7b + 1 fix
# task is ambigous, there is no mentioning of trailing spaces
# please fix, i thought that something wrong with macos but got
# same result on docker offilial image, and i was wery upsate abought this!

def custom_write(file_name, strings):
    positions = {}
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            for index, string in enumerate(strings, start=1):
                # Записываем строку в файл
                start_position = file.tell()
                file.write(f"{string} \n")
                # Сохраняем позицию начала текущей строки
                positions[(index, start_position)] = string
    except IOError as e:
        print(f"Ошибка ввода/вывода: {e}")
    return positions

# Пример использования функции:
info =[
    "Text for tell.",
    "Используйте кодировку utf-8.",
    "Because there are 2 languages!",
    "Спасибо!",
]

result = custom_write("test.txt", info)
for elem in result.items():
    print(elem)
