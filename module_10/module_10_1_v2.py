#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
import os
import time
import multiprocessing as mp
from multiprocessing.pool import ThreadPool, Pool
from threading import Thread

c_count = mp.cpu_count()

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

complexity_multiplier = 10

job_spec = [
    (1 * complexity_multiplier, "example5.txt"),
    (3 * complexity_multiplier, "example6.txt"),
    (20 * complexity_multiplier, "example7.txt"),
    (10 * complexity_multiplier, "example8.txt"),
]
p_timer = PerfTimer()


# all code above is executed in every process!

if __name__ == "__main__":
    # code below is executed only in main process!
    file_cleanup()
    p_timer.start()
    # Запуск функций без процессов/потоков
    print("Работа функций началась.")
    for args in job_spec: 
        write_words(*args)
    p_timer.stop()
    print(f"Время работы функций без процессов/потоков: {p_timer.elapsed_time} c")
    file_cleanup()
    
    # Создание и запуск потоков с аргументами из задачи
    p_timer.start()
    threads = [Thread(target=write_words, args=(args[0], args[1])) for args in job_spec]
    p_timer.stop()
    print(f"Инициализация потоков закончилась за {p_timer.elapsed_time} c")
    print("\nРабота потоков началась.")
    p_timer.start()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    p_timer.stop()
    print(f"Работа потоков закончилась за {p_timer.elapsed_time} c")
    file_cleanup()
    
    # Взятие текущего времени до начала функций
    p_timer.start()
    print("\nРабота функций запити в процессах началась.")
    
    # Запуск функций с аргументами из задачи
    p_timer.start()
    processes = [
        mp.Process(target=write_words, args=(args[0], args[1])) for args in job_spec
    ]
    p_timer.stop()
    print(f"Инициализация процессов закончилась за {p_timer.elapsed_time} c")
    for process in processes:
        process.start()
    for process in processes:
        process.join()  # Ожидание завершения каждого процесса

    p_timer.stop()
    print(f"Работа процессов закончилась за {p_timer.elapsed_time} c")
    file_cleanup()
    time.sleep(5)
    print("\nРабота функций в пуле процессов началась.")
    p_timer.start()
    # использование пула процессов (CPU bount случай)
    with Pool(c_count) as pool:
        p_timer.stop()
        print(f"Инициализация пула процессов закончилась за {p_timer.elapsed_time} c")
        p_timer.start()
        for result in pool.starmap(write_words, job_spec):
            # получение результата (шпаргалка)
            pass
        p_timer.stop()
        print(f"Работа пула процессов закончилась за {p_timer.elapsed_time} c")
    file_cleanup()

    print("\nРабота функций в пуле потоков началась.")
    p_timer.start()
    # использование пула потоков (IO bound)
    with ThreadPool(c_count) as pool:
        p_timer.stop()
        print(f"Инициализация пула потоков закончилась за {p_timer.elapsed_time} c")
        p_timer.start()
        for result in pool.starmap(write_words, job_spec):
            # получение результата (шпаргалка)
            pass
        p_timer.stop()
    print(f"Работа пула потоков закончилась за {p_timer.elapsed_time} c")
    file_cleanup()
