x=int(input("Введите число x: "))
y=int(input("Введите число y: "))
if x==4 and y<2:
    q=x+x*y
elif x<y:
    q=y**2
else:
    q=y**2+4
print("Ответ:", q)