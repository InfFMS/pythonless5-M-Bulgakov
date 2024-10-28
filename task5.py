# Введите массив длины N с клавиатуры и найдите (за один проход)
# количество элементов, имеющих максимальное значение.

N = int(input())
a = int(input())
k=1
for i in range(N-1):
    b = int(input())

    if a == b:
        k += 1

    if b>a:
        k = 1
        a = b

print(k)
