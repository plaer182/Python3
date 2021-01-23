#!/usr/bin/env python3
"""
    Написать программу которая будет симулировать результаты
    производительности запросов в БД а также подсчитывать статистику,
    среднее, максимальное и минимальное из полученных значений.
    Программа должна состоять из следующих функций:
    a. stress_db() - в течении 10 секунд, один раз в секунду функция
    “просыпается” и печатает на экран, а также добавляет в список(list)
    строки в следующем формате:
    current date [time] - <latency, N>, где N: [ 1, 100]
    Например:
    2020/09/30 [02:34:56] - <latency=100>
    2020/09/30 [02:34:57] - <latency=22>
    b. parse_stress_results(list_of_results) - list_of_results это список
    полученный от stress_db(). Функция анализирует список строк и
    возвращает новый список, состоящий из значений latency. Например:
    [100, 22]
    c. calculate_and_print_statistics(latencies) - latencies список
    “нормализованных” значений который вернула parse_stress_results.
    Эта функция вычисляет и печатает статистики: min, max, average.
    Например:
    Minimum latency: 10 ms
    Maximum latency: 100 ms
    Average latency: 55 ms
"""
import datetime
import random
import time


def stress_db():
    list_of_results = []
    for i in range(10):
        time.sleep(1)

        time_now = datetime.datetime.now()
        str_current_date = time_now.strftime("%Y/%m/%d")
        str_time = time_now.strftime("[%H:%M:%S]")

        n = random.randint(1, 100)

        str_stress_db = str_current_date + ' ' + str_time + ' - <latency=' + str(n) + '>'
        print(str_stress_db)
        list_of_results.append(str_stress_db)
    return list_of_results


def parse_stress_db(list_of_results):
    latencies = []
    for line in list_of_results:
        date, value = [s.strip() for s in line.split("-")]
        key, value = value.strip("<>").split("=")
        latencies.append(int(value))
        return latencies


def calculate_and_print_statistics(latencies):
    minimum = min(latencies)
    maximum = max(latencies)
    average = sum(latencies)/len(latencies)
    print(f"Minimum latency: {minimum} ms")
    print(f"Maximum latency: {maximum} ms")
    print(f"Average latency: {average} ms")


if __name__ == '__main__':
    results_of_executing = stress_db()
    latency = parse_stress_db(results_of_executing)
    calculate_and_print_statistics(latency)
