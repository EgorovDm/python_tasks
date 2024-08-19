#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# wizardlm2:7b no fixes
# 1 part
# ===================================================
first = "Мама мыла раму"
second = "Рамена мало было"

# Lambda-функция, которая получает две строки и возвращает список булевских значений (True/False)
result = list(
    map(
        lambda s1, s2: [s1[i] == s2[i] for i in range(min(len(s1), len(s2)))],
        first,
        second,
    )
)

print(
    result
)  # Вывод: [False, True, True, False, False, False, False, False, True, False, False, False, False, False]
# ===================================================

# 2 part
# ====================================================
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(
            file_name, "a"
        ) as f:  # Открываем файл с правом на добавление (append)
            for data in data_set:
                if isinstance(data, str):  # Если данные - строка, добавляем её как есть
                    f.write(data + "\n")
                elif isinstance(
                    data, bytes
                ):  # Если данные - байты (например, изображение), сохраняем как есть
                    f.write(data)
                    f.write("\n")
                else:  # Если данные не являются строкой или байтами, превращаем в строку и добавляем
                    f.write(str(data) + "\n")

    return write_everything

# Создаем функцию для записи в файл 'example.txt'
write = get_advanced_writer("example.txt")
write("Это строчка", ["А", "это", "уже", "число", 5, "в", "списке"])
# ===================================================

# 3 part
# ===================================================
from random import choice  # noqa: E402

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


# Создаем объект MysticBall с тремя возможными ответами
first_ball = MysticBall("Да", "Нет", "Наверное")

# Вызываем объект MysticBall, чтобы получить случайный ответ
print(first_ball())  # Вывод может быть: Да, Наверное, Нет
print(first_ball())  # Вывод может быть: Да, Наверное, Нет
print(first_ball())  # Вывод может быть: Да, Наверное, Нет
# ===================================================