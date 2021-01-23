"""
    Два списка целых заполняются случайными числами(использовать нужную функцию из модуля random). Необходимо:
    a. Сформировать третий список, содержащий элементы обоих списков
    b. Сформировать третий список, содержащий элементы обоих списков без повторений;
    c. Сформировать третий список, содержащий элементы общие для двух списков;
    d. Сформировать третий список, содержащий только уникальные элементы каждого из списков;
    e. Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков.
"""
import random
first_random_number = int(input("Enter first random number: "))
len_first_list = int(input("Enter length of the first list: "))
second_random_number = int(input("Enter second random number: "))
len_second_list = int(input("Enter length of the second list: "))
operation = input("Enter operation [a, b, c, d, e]: ")

list_1 = [random.randint(0, first_random_number) for i in range(len_first_list)]
list_2 = [random.randint(0, second_random_number) for j in range(len_second_list)]

print(f"List_1: {list_1}")
print(f"List_2: {list_2}\n")

if operation == "a":
    print(f"List_a: {list_1 + list_2}")

elif operation == "b":
    list_b = list_1 + [b for b in list_2 if b not in list_1]
    for i in range(len(list_b)):
        while list_b.count(i) > 1:
            list_b.remove(i)
    print(f"List_b: {list_b}")

elif operation == "c":
    list_c = [i for i in list_1 if i in list_2]
    print(f"List_b: {list_c}")

elif operation == "d":
    list_d = [i for i in list_1 + list_2 if i not in list_1 or i not in list_2]
    for i in range(len(list_d)):
        while list_d.count(i) > 1:
            list_d.remove(i)
    print(f"List_d: {list_d}")

elif operation == "e":
    list_e = [min(list_1), max(list_1), min(list_2), max(list_2)]
    print(f"List_e: {list_e}")

else:
    print(f"Error: unknown operation symbol: {operation}")
