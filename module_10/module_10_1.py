#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
import os
import time
from threading import Thread

# класс таймер для удобной работы
class PerfTimer:
    """Class for measuring execution time of a code block.

    Attributes:
        _start (float): Timepoint when the timer started.
        _end (float): Timepoint when the timer stopped.
        elapsed_time (float): Time difference between stop and start.
    """
    def __init__(self) -> None:
        self._start = 0.0
        self._end = 0.0
    
    def start(self) -> None:
        """Start the timer, recording the current time as the start time."""
        self._start = time.perf_counter()
        self._end = self._start

    def stop(self) -> None:
        """Stop the timer, recording the current time as the end time."""
        self._end = time.perf_counter()

    @property
    def elapsed_time(self):
        """Calculate and return the time elapsed between the start and stop moments."""
        return self._end - self._start

def write_words(word_count, file_name):
    with open(file_name, "w") as f:
        for word_id in range(word_count):
            word = f"Какое-то слово № {word_id + 1}"
            f.write(f"{word}\n")
            time.sleep(0.1)  # Пауза на 0.1 секунды
        print(f"Завершилась запись в файл {file_name}")

def file_cleanup() -> None:
    for file_name in glob.iglob("example*.txt"):
        os.remove(file_name)

job_spec = [
    (10, "example1.txt"),
    (30, "example2.txt"),
    (200, "example3.txt"),
    (100, "example4.txt")
]
file_cleanup()

p_timer = PerfTimer()

print("Работа функций началась.")
p_timer.start()
# Запуск функций без процессов/потоков
for args in job_spec: 
    write_words(*args)

p_timer.stop()
print(f"\nВремя работы функций без процессов/потоков: {p_timer.elapsed_time}")
file_cleanup()

# Создание и запуск потоков с аргументами из задачи

threads = [
    Thread(target=write_words, args=(args[0], args[1])) for args in job_spec
]
print("Работа потоков началась.")
p_timer.start()
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
p_timer.stop()
print(f"Работа потоков закончилась за {p_timer.elapsed_time}")
file_cleanup()
