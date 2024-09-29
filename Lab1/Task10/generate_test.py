import random
n = 100000
ord_A = ord('A')
ord_Z = ord('Z')
a = [chr(random.randint(ord_A, ord_Z)) for _ in range(n)]
with open('input.txt', 'wt') as f:
    f.write(str(n) + '\n')
    f.write(''.join(a))
