#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
from time import sleep

class Knight(threading.Thread):
    def __init__(self, name, power, enemy_count=100):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy_count = enemy_count
        self.local_enemies = enemy_count
        self.day_counter = 0
        self.start()  # Запускаем поток

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.local_enemies > 0:
            enemies_killed = min(self.local_enemies, self.power)
            self.local_enemies -= enemies_killed
            self.day_counter += 1
            print(
                f"{self.name}, сражается {self.day_counter} день(дня)..., осталось {self.local_enemies} воинов."
            )
            sleep(1)  # Задержка на 1 секунду
            if self.local_enemies == 0:
                print(
                    f"{self.name} одержал победу спустя {self.day_counter} дней(дня)!"
                )
                return None

if __name__ == "__main__":
    first_knight = Knight("Sir Lancelot", 10)
    second_knight = Knight("Sir Galahad", 20)

    # Останавливаем текущий поток, чтобы отслеживать вывод и затем возобновлять его
    first_knight.join()
    second_knight.join()
    print("Все битвы закончились!")
