#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# wizardlm2:7b + no fixes (simple task)

def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        try:
            # Получаем имя функции для ключа в словаре
            function_name = func.__name__
            # Применяем функцию к int_list и сохраняем результат в словаре
            results[function_name] = func(int_list) if callable(func) else None
        except Exception as e:
            print(f"Ошибка при выполнении функции '{func.__name__}': {e}")
    return results


# Пример использования функции apply_all_func
if __name__ == "__main__":
    # Пример 1: Вызов функций min и max
    result1 = apply_all_func([6, 20, 15, 9], max, min)
    print(result1)

    # Пример 2: Вызов функций len, sum и sorted
    result2 = apply_all_func([6, 20, 15, 9], len, sum, sorted)
    print(result2)
