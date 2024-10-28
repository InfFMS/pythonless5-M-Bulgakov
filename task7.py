# Заполнить массив длины N случайными числами в интервале [-100,100] и
# переставить элементы так, чтобы все положительные элементы
# стояли в начала массива, а все отрицательные и нули в конце.
# Пример: ввод N = 6
# [20, -90, 15, -34, 10, 0]
# Вывод: [20, 15, 10, -90, -34, 0]

'''
import random
from colored import fg

N = int(input())
m = []
for j in range(N):
    m=[]
    for i in range (N):
        k = random.randint(32, 126)
        m.append(chr(k))
        color = fg('green')
        print(color + chr(k), end="")
'''

import random
N = int(input())
m = []
j = []
f = 0
for i in range (N):
    k = random.randint(0, 100)
    z = random.randint(0, 1)
    if z == 0:
        l = k*(-1)
        k=l
    if k>0:
        m.append(k)
    else:
        j.append(k)

print(m+j)