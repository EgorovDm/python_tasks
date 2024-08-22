#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for _ in range(100):
            amount = randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()  # Разблокируем если баланс больше или равен 500
            self.balance += amount
            print(f"Пополнение: {amount}. Баланс: {self.balance}")
            sleep(.001)
    
    def take(self):
        for _ in range(100):
            amount = randint(50, 500)
            if amount <= self.balance:
                with self.lock:
                    self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")
            else:
                print(f"Запрос отклонён, недостаточно средств")
                self.lock.acquire()

if __name__ == "__main__":
    bk = Bank()
    th1 = Thread(target=Bank.deposit, args=(bk,))
    th2 = Thread(target=Bank.take, args=(bk,))

    print("Банковские операции в процессе...")
    th1.start()
    th2.start()
    th1.join()
    th2.join()

    print(f"Итоговый баланс: {bk.balance}")
