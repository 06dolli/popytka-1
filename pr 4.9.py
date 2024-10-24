n=int(input("Введите количество чисел из ряда Фибоначчи: "))
a=0
b=1
s=0
for i in range(n):
    s+=a
    a, b = b, a + b
print(s)