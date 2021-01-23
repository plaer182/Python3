#!/usr/bin/env python3
"""
    Simple gematria - написать программу которая будет проверять являются ли
    два слова гематрически равными (слова написаны латинскими буквами,
    маленькие буквы равны большим, a-1, b-2, …, z-26 ). Решение должно
    состоять из двух функций, одна вычисляет гематрическое значение слова,
    другая сравнивает значения и выдает результат на экран. Пример bentsi и
    darwin гематрически равны.
"""


def gem_sum(word):
    for i in word:
        if i == i.upper():
            word = word.lower()
    gem_value = sum([(ord(i) - 96) for i in word])
    return gem_value


def compare_gem_sum(word_1, word_2):
    if gem_sum(word_1) == gem_sum(word_2):
        print(f"{word_1} in Simple Gematria equals: {gem_sum(word_1)}")
        print(f"{word_2} in Simple Gematria equals: {gem_sum(word_2)}")
        print(f"{word_1} and {word_2} are gematrically equal")
    else:
        print(f"{word_1} in Simple Gematria equals: {gem_sum(word_1)}")
        print(f"{word_2} in Simple Gematria equals: {gem_sum(word_2)}")
        print(f"{word_1} add {word_2} are not gematrically equal")


if __name__ == '__main__':
    compare_gem_sum(word_1="Winter", word_2="Summer")
    compare_gem_sum(word_1="Spring", word_2="Autumn")
