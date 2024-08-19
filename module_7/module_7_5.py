#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# wizardlm2:7b + fixes for symlinks (which are important concept for proper unix systems)
# Обратите внимание, что в Python 3.3 и выше модуль datetime предоставляет 
# функцию datetime.now(), которая может быть использована вместо 
# time.localtime(filetime) для получения текущего времени или для работы 
# с датами и временем. В примере выше я использовал datetime.fromtimestamp(filetime) 
# для получения даты и времени, соответствующей время последнего изменения файла.

import os
from datetime import datetime
import sys

def walk_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Получаем полный путь к файлу
            filepath = os.path.join(root, file)
            # Получаем родительскую директорию файла
            parent_dir = os.path.dirname(filepath)
            # Получаем время последнего изменения файла
            if not os.path.islink(filepath):
                filetime = os.path.getmtime(filepath)
                # Преобразуем время в строку с форматом 'dd.mm.yyyy HH:MM'
                formatted_time = datetime.fromtimestamp(filetime).strftime("%d.%m.%Y %H:%M")
                # Получаем размер файла в байтах
                filesize = os.path.getsize(filepath)
                # Выводим информацию о файле
                print(
                    f"Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}"
                )
            else:
                print(
                    f"Обнаружена ссылка: {file}, Путь: {filepath}, Родительская директория: {parent_dir}, на {os.readlink(filepath)}"
                )

# Укажите путь к директории для обхода
directory = sys.argv[1] if len(sys.argv) > 1 else "."
walk_directory(directory)
