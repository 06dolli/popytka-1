n=int(input("Введите количество чисел из ряда Фибоначчи: "))
k=int(input("Введите порядковый номер, с которого нужно начать: "))
a=0
b=1
s=0
for i in range(k+1):
    if i >=k-1:
        s+=a
    a, b = b, a + b
print(s)