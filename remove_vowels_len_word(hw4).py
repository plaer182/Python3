#!/usr/bin/env python3
"""
    Следующие задачи поместить в один файл:
    a. Написать функцию remove_vowels(sentence) которая получает string и
    возвращает новый string в котором все гласные удалены.
    b. Написать функцию которая принимает предложение и возвращает
    список списков в котором будут слова и кол символов в слове.
    Например: “ It's no use going back to yesterday, because I was a different
    person then.” -> [ [“It's”, 3], [“no”, 2], [“use”, 3], . . . , [“then.”, 4] ]
"""


def remove_vowels(sentence):
    vowels = 'AaEeIiOoUuYyАаУуОоЫыИиЭэЯяЮюЁёЕе'
    for i in sentence:
        if i in vowels:
            sentence = sentence.replace(i, "")
    return sentence


def list_word_len_word(sentence):
    str_len_list = [[line, len(line)] for line in sentence.split(' ')]
    return str_len_list


if __name__ == "__main__":
    print(remove_vowels(sentence="Winter is already here"))
    print(list_word_len_word(sentence="Winter is already here"))
