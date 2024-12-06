def findmax():
    num=int(input("Введите натуральное число (0 для завершения): "))
    if num==0:
        return float('-inf') #отрицательная бесконечность (любое натуральное число больше)
    else:
        return max(num, findmax())
maxx=findmax()
print("Наибольшее число в последовательности:", maxx)
