m=[]
a=input('Введите 1 целое число \n')
b=input('Введите 2 целое число \n') 
c=input('Введите 3 целое число \n')
if 1<=int(a)<=3:
    m.append(a)
elif 1<=int(b)<=3:
    m.append(b)
elif 1<=int(c)<=3:
    m.append(c)
if len(m)<=0:
    print("Чисел входящих в промежуток нет")
else:
    print ('Числа входящие в промежуток:', ''.join(m))