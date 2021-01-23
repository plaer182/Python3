#!/usr/bin/env python3
"""
    Написать программу которая принимает список имен и возвращает новый
    список в котором к каждому имени будет добавлен суффикс рандомного
    валютного символа [“$” , “€”, “₽”, “₪”]. Количество валютных символов
    должно быть равно количеству букв в имени. Имя может содержать только
    большие и маленькие буквы английского алфавита. Максимальная длина
    имени 40 символов. В решении использовать генератор map. Выбросить
    exceptions для некорректного ввода. Написать как минимум 2 позитивных и
    2 негативных теста (в отдельном файле.)
"""
import random
import string


def random_symbol(list_of_names):
    for line in list_of_names:
        for elem in line:
            if elem not in string.ascii_letters:
                raise Exception("Names contain not only English letters")
    for i in list_of_names:
        if len(i) > 40:
            raise Exception("Maximum name length exceeded")

    symbols = ['$', '€', '₽', '₪']
    map_list = list(map(lambda x: x + random.choice(symbols) * len(x), list_of_names))
    result_list = [str(i) for i in map_list]
    return result_list


if __name__ == '__main__':
    list_names = ["Anna", "Boris", "Evgenia", "Viktor"]
    print(random_symbol(list_names))
