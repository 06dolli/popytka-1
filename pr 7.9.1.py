def summ(n):
    return sum(int(x) for x in str(n))
def zero(n):
    k=0
    while n>0:
        n-=summ(n)
        k+=1
    return k
number=int(input("Введите число: "))
result=zero(number)
print("Количество действий до нуля:", result)
