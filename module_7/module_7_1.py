#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# wizardlm2:7b + 2 fixes

import csv
from typing import List


class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self) -> str:
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    __FILE_NAME = "products.txt"

    def __init__(self):
        self.products = []

    def get_products(self) -> str:
        try:
            with open(Shop.__FILE_NAME, mode="r", encoding="utf-8") as file:
                reader = csv.reader(file)
                return "\n".join([", ".join(row) for row in reader])
        except FileNotFoundError:
            return ""

    def add(self, *products: List["Product"]):
        try:
            with open(Shop.__FILE_NAME, mode="r+", encoding="utf-8") as file:
                reader = csv.reader(file)
                data = list(reader)
                writer = csv.writer(file)
                for product in products:
                    if all(product.name != row[0] for row in data):
                        data.append(
                            [str(product.name), str(product.weight), product.category]
                        )
                        file.seek(0)
                        writer.writerows(data)
                        print(f'Продукт "{product.name}" добавлен в магазин')
                    else:
                        print(f'Продукт "{product.name}" уже есть в магазине')
        except FileNotFoundError:
            with open(Shop.__FILE_NAME, mode="w", encoding="utf-8") as file:
                writer = csv.writer(file)
                added_products = []
                for product in products:
                    if product.name not in added_products:
                        added_products.append(product.name)
                        writer.writerow(
                            [str(product.name), str(product.weight), product.category]
                        )
                    else:
                        print(f'Продукт "{product.name}" уже есть в магазине')


# Пример использования классов:

s1 = Shop()
p1 = Product("Potato", 50.5, "Vegetables")
p2 = Product("Spaghetti", 3.4, "Groceries")
p3 = Product("Potato", 5.5, "Vegetables")

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())

