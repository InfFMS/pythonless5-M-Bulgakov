# Заполнить массив длины N случайными числами в диапазоне от 10 до 100000 и
# отобрать в другой массив все числа, которые состоят из одинаковых цифр.
# Используйте для этого логическую функцию.
# Пример: ввод N = 4
# [12, 77, 5555, 97]
# Вывод: [77, 5555]

import random
N = int(input())
m = []
f = 0
for i in range (N):
    k = random.randint(10, 100000)
    if (k%11 == 0 and k < 100) :
        m.append(k)
    elif (k%111 ==0 and k>100 and k<1000):
        m.append(k)
    elif (k%1111 == 0 and k>1000 and k < 10000):
        m.append(k)
    elif k%11111==0:
        m.append(k)

print(m)