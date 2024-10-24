n=10
a=[]
b=[]
for i in range(n):
    x=input("Введите элемент массива а:")
    a.append(x)
for j in range(n):
    y=input("Введите элемент массива b:")
    b.append(y)
a2=[]
b2=[]
a2=a
b2=b
print("Массив a до преобразования:", ''.join(map(str, a2)))
print("Массив b до преобразования:", ''.join(map(str, b2)))
print()
a=b2
b=a2
print("Массив a после преобразования:", ''.join(map(str, a)))
print("Массив b после преобразования:", ''.join(map(str, b)))
