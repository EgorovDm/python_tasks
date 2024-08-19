#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# wizardlm2:7b

def all_variants(text):
    # Функция для создания генератора подпоследовательностей
    def substrings(*args):
        text = args[0] if len(args) > 0 else ""
        for i in range(len(text)):
            for j in range(i + 1, len(text) + 1):
                yield text[i:j]
    # Возвращаем объект-генератор, который генерирует подпоследовательности
    return substrings(text)

# Пример использования функции all_variants
if __name__ == "__main__":
    a = all_variants("abc")
    for i in a:
        print(i)
