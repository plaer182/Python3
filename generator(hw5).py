#!/usr/bin/env python3
"""
    Cycle generator
    написать generator функцию cycle которая будет получать iterable и
    возвращать элементы iterable по кругу бесконечно. Например cycle([1,2,3])
    будет возвращать 1,2,3,1,2,3,1,....∞ пока не прервется цикл.

    Написать функцию iter_n_times(iterable, n) которая будет получать iterable и
    возвращать iterable с n повторениями. например iter_n_times(iterable=“abc”,
    n=2) будет возвращать: “abcabc”
"""


def cycle(iterable):
    while True:
        for i in iterable:
            yield i


def iter_n_times(iterable, n):
    cycle_iter = cycle(iterable)
    iter_type = type(iterable)
    result = (next(cycle_iter) for _ in range(n * len(iterable)))
    return iter_type(result) if iter_type is not str else str().join(result)


if __name__ == '__main__':
    # for elem in cycle([1, 2, 3]):
    #     print(elem)
    print(iter_n_times([1, 2, 3], 5))
    print(iter_n_times("abc", 5))
