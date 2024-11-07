n=int(input("Введите порядок матрицы n: "))
import random
def sm(n, low=-10, high=10): #low и high: это диапазон значений, в котором будут находиться случайные числа
    return [[random.uniform(low, high) for _ in range(n)] for _ in range(n)] # создаёт случайное вещественное число 

def mn(matrix):
    maxx=0
    max_index = (-1, -1)
    for i in range(len(matrix)): # возвращаю количество строк
        for j in range(len(matrix[i])): # возвращаю количество элементов в строке
            if abs(matrix[i][j])>abs(maxx):
                maxx=matrix[i][j]
                max_index=(i, j)

    # Формирую новую матрицу n-1
    newmatrix = [
        row[:max_index[1]] + row[max_index[1]+1:] #включая все элементы с новым значение и значением после него
        for i, row in enumerate(matrix) if i != max_index[0] #строки, исключая строки с макс элементом
    ]
    return maxx, newmatrix

def print_matrix(matrix):
    for row in matrix:
        print(" | ".join(f"{value:5.3f}" for value in row))  # чтобы каждое число занимало 5 символов, с 3 знаками после запятой


matrix=sm(n)
print('Исходная матрица порядка', n, ':')
for row in matrix:
        print(" | ".join(f"{value:5.3f}" for value in row))  # чтобы каждое число занимало 5 символов, с 3 знаками после запятой


maxx, newmatrix=mn(matrix)
print("\nНаибольший по модулю элемент:", maxx)
print("Матрица после удаления строки и столбца:")
print_matrix(newmatrix)

