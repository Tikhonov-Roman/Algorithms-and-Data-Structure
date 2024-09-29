# -*- coding: utf-8 -*-
from time import time

start_time = time()
with open("input.txt") as f:
    n = int(f.readline())
    if n < 1 or n > 100000:
        with open('output.txt', 'wt') as answer_f:
            answer_f.write("Введено некорректное значение n")
        exit()
    a = f.readline()
    ord_A = ord("A")
    d = [0] * (ord("Z") - ord_A + 1)
    for elem in a:
        d[ord(elem) - ord_A] += 1
    left = center = ""
    for i in range(len(d)):
        letter, cnt = chr(i + ord_A), d[i]
        tmp = letter * (cnt // 2)
        left += tmp
        if center == "" and cnt % 2 == 1:
            center = letter
    right = left[::-1]

    with open('output.txt', 'wt') as answer_f:
        answer_f.write(left + center + right)
stop_time = time()
if stop_time - start_time <= 1:
    print("Время выполнения:", stop_time - start_time, 's')
else:
    print("Превышено время выполнения:", stop_time - start_time, 's')
