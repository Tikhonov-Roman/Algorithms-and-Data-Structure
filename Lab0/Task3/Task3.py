from time import time
start = time()
with open('input.txt') as f:
    n = int(f.readline())
    answer = 0
    if 1 <= n <= 2:
        answer = 1
    else:
        
        a = [1, 1]
        answer = 2
        for i in range(n - 2):
            answer = (a[0] + a[1]) % 10
            a[0] = a[1]
            a[1] = answer
        
    answer_f = open('output.txt', 'wt')
    answer_f.write(str(answer))
    answer_f.close()
print("Execution time:", time() - start, 'ms')
