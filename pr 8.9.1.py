import random
a=[]
k=int(input("Введите число k: "))
size=int(input("Введите сторону квадрата: "))
matrix=[[random.randint(1, 70) for _ in range(size)] for _ in range(size)] #каждая строка имеет size элементов, и таких строк тоже size

def kr(matrix, k):
    count=0
    maxx=0

    for row in matrix: #для каждой строки в матрице
        for element in row: #для каждого эелемента матрицы
            if element%k==0:
                count+=1
                if maxx==0 or element>maxx:
                    maxx=element
                    
    return count, maxx
count, maxx=kr(matrix, k)
print("Текущая матрица: ", matrix, 'число элементов кратных', k, ':', count, 'Максимальное число:', maxx)