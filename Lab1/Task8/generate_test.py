import random
n = 5000
mn_elem = -10 ** 9
mx_elem = 10 ** 9
a = [str(random.randint(mn_elem, mx_elem)) for _ in range(n)]
with open('input.txt', 'wt') as f:
    f.write(str(n) + '\n')
    f.write(' '.join(a))
