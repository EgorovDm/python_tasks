#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# wizardlm2:7b + fixes

import threading
import random
import queue
from time import sleep

class Table:
    def __init__(self, number: int):
        self.number = number
        self.guest = None

    def seat_guest(self, guest):
        print(f"{guest.name} сел(-а) за стол номер {self.number}")
        self.guest = guest
        guest.start()

    def is_free(self) -> bool:
        non_guest = self.guest is None
        if (not non_guest) and (not self.guest.is_alive()):
            self.guest = None
        return non_guest

class Guest(threading.Thread):
    def __init__(self, name: str):
        super().__init__(target=self.run)
        self.name = name

    def run(self):
        sleep(random.uniform(3, 10))  # Задержка от 3 до 10 секунд
        self.eat()

    def eat(self):
        print(f"{self.name} покушал(-а) и ушёл(ушла)")


class Cafe:
    def __init__(self, *tables: Table):
        self.queue = queue.Queue()
        self.tables = set(tables)

    def guest_arrival(self, *guests: Guest):
        for guest in guests:
            c_table = self.find_free_table()
            if c_table:
                c_table.seat_guest(guest)
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty():    
            c_table = self.find_free_table()
            if c_table:
                c_table.seat_guest(
                    self.queue.get()
                )
            else:
                pass
        for table in self.tables:
            table.guest.join()
        print("Все гости ушли")

    def find_free_table(self) -> bool:
        for table in list(self.tables):
            if table.is_free():
                return table
        return None

if __name__ == "__main__":
    tables = [Table(number) for number in range(1, 6)]
    guests_names = [
        "Maria",
        "Oleg",
        "Vakhtang",
        "Sergey",
        "Darya",
        "Arman",
        "Vitoria",
        "Nikita",
        "Galina",
        "Pavel",
        "Ilya",
        "Alexandra",
    ]
    guests = [Guest(name) for name in guests_names]
    cafe = Cafe(*tables)

    cafe.guest_arrival(*guests)
    cafe.discuss_guests()
