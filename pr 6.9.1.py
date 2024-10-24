n=int(input('Введите размер массива:'))
a=[]
for i in range(n):
    x=input("Введите элемент массива:")
    a.append(x)
a2=sorted(a)
print("Минимальный эллемент:", a2[0])
print("Массив наоборот:", ''.join(map(str, a[::-1])))
