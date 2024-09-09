from time import time
start = time()
with open('input.txt') as f:
    n = int(f.readline())
    answer = 0
    if 1 <= n <= 2:
        answer = 1
    elif n > 2:
        
        a = b = 1
        
        for i in range(n - 2):
            a, b = b, a + b
        answer = b 
    answer_f = open('output.txt', 'wt')
    answer_f.write(str(answer))
    answer_f.close()
print("Execution time:", time() - start, 'ms')

