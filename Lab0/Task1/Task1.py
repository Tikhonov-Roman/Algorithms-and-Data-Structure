#1.1
a, b = map(int, input().split())
print(a + b)
#1.2
a, b = map(int, input().split())
print(a + b ** 2)
#1.3
with open('input.txt') as f:
    a, b = map(int, f.readline().split())
    answer_f = open('output.txt', 'wt')
    answer_f.write(str(a + b))
    answer_f.close()
#1.4
with open('input2.txt') as f:
    a, b = map(int, f.readline().split())
    answer_f = open('output2.txt', 'wt')
    answer_f.write(str(a + b **2 ))
    answer_f.close()
    
