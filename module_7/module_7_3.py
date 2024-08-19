#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# wizardlm2:7b + 2 fixes

import re

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            words = []
            with open(file_name, "r", encoding="utf-8") as file:
                for line in file:
                    # Преобразуем строку в нижний регистр и удаляем пунктуацию
                    line_words = re.sub(r"[,\.\?\;\:\-\ ]+", " ", line.lower())
                    words.extend(line_words.split())  # Добавляем слова в список
            all_words[file_name] = words
        return all_words

    def find(self, word):
        result = {}
        for file_name, words in self.get_all_words().items():
            try:
                print(words)
                print(word.lower())
                index = words.index(word.lower())
            except ValueError:
                # Слово не найдено в списке
                index = None
            result[file_name] = index
        return result

    def count(self, word):
        result = {}
        for file_name, words in self.get_all_words().items():
            result[file_name] = words.count(word.lower())
        return result


# Пример использования класса WordsFinder:
finder2 = WordsFinder("test.txt")
print(finder2.get_all_words())  # Все слова
position = finder2.find("TEXT")
print(position)  # Позиция 'TEXT' в каждом файле
count = finder2.count("teXT")
print(count)  # Количество 'teXT' в 'test.txt'
