#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            amount = randint(50, 500)
            with self.lock:
                if self.balance >= 500 and not self.lock.locked():
                    self.lock.release()  # Разблокируем если баланс больше или равен 500
                self.balance += amount
            print(f"Пополнение: {amount}. Баланс: {self.balance}")
            sleep(0.001)

    def take(self):
        for _ in range(100):
            amount = randint(50, 500)
            if amount <= self.balance:
                with self.lock:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
            else:
                print(f"Запрос отклонён, недостаточно средств")
                #with self.lock:
                #    if self.balance + amount >= 500:
                #        self.lock.acquire()  # Заблокируем если попытка снятия при недостаточном балансе

if __name__ == "__main__":
    bk = Bank()
    th1 = threading.Thread(target=bk.deposit)
    th2 = threading.Thread(target=bk.take)

    print("Банковские операции в процессе...")
    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(f"Итоговый баланс: {bk.balance}")
