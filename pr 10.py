a = []
n =3
with open("vvod.txt") as f:
    for line in f:
        arr = [int(x.strip()) for x in line.split()]
        a.append(arr)

for i in a:
    print(*i)
k=int(input("Введите число k: "))

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
count, maxx=kr(a, k)
print("Текущая матрица: ", a, 'число элементов кратных', k, ':', count, 'Максимальное число:', maxx)

fv = open('vivod.txt', 'w')#перезапись данных
fv.write('число элементов кратных: ' + str(count)+ '\n')
fv.write('Максимальное число: ' + str(maxx))
fv.close()