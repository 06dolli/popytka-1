import math
def per(a, b, c):
    p=(a+b+c)/2
    s=math.sqrt(p*(p-a)*(p-b)*(p-c))
    return s
a=float(input("Введите первую сторону треугольника: "))
b=float(input("Введите вторую сторону треугольника: "))
c=float(input("Введите третью сторону треугольника: "))
if a+b>c and a+c>b and b+c>a:
    s=per(a, b, c)
    print("Площадь треугольника: ", s)
else:
    print("Треугольник с такими сторонами не существует")

