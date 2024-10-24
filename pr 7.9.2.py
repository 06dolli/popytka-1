import math
n=int(input('Введите размер массива:'))
a=[]
b=[]
c=[]
for i in range(n):
    x=int(input("Введите элемент массива 1:"))
    a.append(x)
for j in range(n):
    y=int(input("Введите элемент массива 2:"))
    b.append(y)
for g in range(n):
    z=int(input("Введите элемент массива 3:"))
    c.append(z)
print('Среднее арифмитическое значение масива 1:', sum(a)/n)
print('Среднее арифмитическое значение масива 2:', sum(b)/n)
print('Среднее арифмитическое значение масива 3:', sum(c)/n)
print('Произведение масива 1:', math.prod(a))
print('Произведение масива 2:', math.prod(b))
print('Произведение масива 3:', math.prod(c))