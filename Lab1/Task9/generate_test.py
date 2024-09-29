import random
n = 10 ** 3

a = [str(random.randint(0, 1)) for _ in range(n)]
a[0] = '1'
b = [str(random.randint(0, 1)) for _ in range(n)]
b[0] = '1'
with open('input.txt', 'wt') as f:
    f.write(''.join(a) + " " + ''.join(b))
