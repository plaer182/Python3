#!/usr/bin/env python3
from random_symbols import random_symbol
import string


def test_length_name():
    """
        Check length of element in list of results
    """
    try:
        random_symbol(["Annannannannannannannannannannannannannannanna", "Boris", "Evgenia", "Viktor"])
    except:
        pass
    else:
        raise Exception("incorrect input accepted or ignored")


def test_correctness():
    """
        Check basic functionality using happy path
    """
    list_of_names_1 = ["Anna", "Boris", "Evgenia", "Viktor"]
    name_plus_symbols = random_symbol(list_of_names_1)
    symbols = '$€₽₪'

    letters_counter = 0
    symbols_counter = 0
    for elem in name_plus_symbols:
        for char in elem:
            if char.isalpha():
                letters_counter += 1
            elif char in symbols:
                symbols_counter += 1
            else:
                if char.isprintable():
                    raise Exception("Unknown type of char: ", char)
                else:
                    raise Exception("Unknown type of char: unprintable ", hex(char))
    assert symbols_counter == letters_counter


def test_incorrectness():
    """
       Check basic functionality using unhappy path
   """
    try:
        random_symbol(["Anna!!", "~Boris~", "Evge,,nia", "Vik/tor"])
    except:
        pass
    else:
        raise Exception("incorrect input accepted or ignored")


if __name__ == '__main__':
    test_length_name()
    test_correctness()
    test_incorrectness()

