mn = -10 ** 9
mx = 10 ** 9
# 1.1
a, b = map(int, input().split())
if (mn <= a <= mx) and (mn <= b <= mx):
    print(a + b)
else:
    print("Введены данные, несоответствующие условию")

# 1.2
a, b = map(int, input().split())
if (mn <= a <= mx) and (mn <= b <= mx):
    print(a + b ** 2)
else:
    print("Введены данные, несоответствующие условию")

# 1.3
with open('input.txt') as f:
    a, b = map(int, f.readline().split())
    answer_f = open('output.txt', 'wt')
    if (mn <= a <= mx) and (mn <= b <= mx):
        answer_f.write(str(a + b))
    else:
        answer_f.write("Введены данные, несоответствующие условию")
    answer_f.close()
# 1.4
with open('input2.txt') as f:
    a, b = map(int, f.readline().split())
    answer_f = open('output2.txt', 'wt')
    if (mn <= a <= mx) and (mn <= b <= mx):
        answer_f.write(str(a + b ** 2))
    else:
        answer_f.write("Введены данные, несоответствующие условию")
    answer_f.close()
