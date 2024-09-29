# -*- coding: utf-8 -*-
from time import time

start_time = time()
with open("input.txt") as f:
    n = int(f.readline())
    if n < 1 or n > 10 ** 3:
        with open('output.txt', 'wt') as answer_f:
            answer_f.write("Введено некорректное значение n")
        exit()
    a = list(map(int, f.readline().split()))
    for elem in a:
        if abs(elem) > 10 ** 9:
            with open('output.txt', 'wt') as answer_f:
                answer_f.write("В массиве имеются числа превосходящие 10^9 по модулю")
            exit()
    for i in range(1, n):
        move_elem = a[i]
        j = i - 1
        while j >= 0 and move_elem < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = move_elem
    with open('output.txt', 'wt') as answer_f:
        answer_f.write(' '.join([str(elem) for elem in a]))
stop_time = time()
if stop_time - start_time <= 2:
    print("Время выполнения:", stop_time - start_time, 's')
else:
    print("Превышено время выполнения:", stop_time - start_time, 's')
