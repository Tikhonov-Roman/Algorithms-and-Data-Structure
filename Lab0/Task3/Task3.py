from time import time

start = time()
mn = 0
mx = 10 ** 7
with open('input.txt') as f:
    n = int(f.readline())
    answer = 0
    if n < mn or n > mx:
        answer = "Введены данные, несоответствующие условию"
    elif 1 <= n <= 2:
        answer = 1
    else:
        a = b = 1
        answer = 2
        for i in range(n - 2):
            a, b = b, (a + b) % 10
        answer = b
    answer_f = open('output.txt', 'wt')
    answer_f.write(str(answer))
    answer_f.close()
print("Execution time:", time() - start, 'ms')
