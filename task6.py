# Массив имеет четное число элементов N.
# Заполнить массив случайными числами и
# выполнить реверс отдельно в первой половине и второй половине.
# Пример: ввод N = 6
# [1,2,3,4,5,6]
# Вывод: [3,2,1,6,5,4]

import random
N = int(input())
m = []
f = 0
for i in range (N):
    k = random.randint(1, 99999)
    m.append(k)

k1 = m[:(N//2)-1:-1]
k2 = m[(N//2)-1::-1]

v = k2 +k1
print(v)