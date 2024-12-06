def recursive(a, b):
    if a<b:
        return a
    return recursive(a-b, b) # Уменьшаю a на b и вызываем функцию снова
a=int(input("Введите значение а: "))
b=int(input("Введите значение b: "))
result=recursive(a, b)
print('Остаток деления', a, 'на', b, 'равен:', result)
