# -*- coding: utf-8 -*-
from time import time

start_time = time()
with open("input.txt") as f, open('output.txt', 'wt') as answer_f:
    n = int(f.readline())
    if n < 1 or n > 5000:
        answer_f.write("Введено некорректное значение n")
        exit()
    a = list(map(int, f.readline().split()))
    for elem in a:
        if abs(elem) > 10 ** 9:
            answer_f.write("В массиве имеются числа превосходящие 10^9 по модулю")
            exit()
    for i in range(0, n - 1):
        mn_idx = i
        for j in range(i + 1, n):
            if a[j] < a[mn_idx]:
                mn_idx = j
        if i != mn_idx:
            a[i], a[mn_idx] = a[mn_idx], a[i]
            answer_f.write(f"Swap elements at indices {i + 1} and {mn_idx + 1}.\n")
    answer_f.write("No more swaps needed.")

stop_time = time()
if stop_time - start_time <= 1:
    print("Время выполнения:", stop_time - start_time, 's')
else:
    print("Превышено время выполнения:", stop_time - start_time, 's')
