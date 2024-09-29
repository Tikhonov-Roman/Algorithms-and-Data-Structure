# -*- coding: utf-8 -*-
from time import time

start_time = time()
with open("input.txt") as f:
    a, b = [[int(x) for x in elem] for elem in f.readline().split()]
    n = len(a)
    if n < 1 or n > 10 ** 3:
        with open('output.txt', 'wt') as answer_f:
            answer_f.write("Введено некорректное число")
        exit()

    c = [0] * (n + 1)
    add = 0
    # Асимптотическое время выполнения O(n)
    for i in range(n - 1, -1, -1):
        elem = a[i] + b[i] + add
        c[i + 1] = elem % 2
        add = elem // 2

    c[0] = add
    with open('output.txt', 'wt') as answer_f:
        answer_f.write(''.join([str(elem) for elem in c]))
print("Время выполнения:", time() - start_time, 's')
