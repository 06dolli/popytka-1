age=int(input("Введите ваш возраст: "))
if age<0 or age>130:
    print("Вы ввели некорректный возраст")
elif age<18:
    print("Вы еще маленький")
elif 18<=age<65:
    print("Вы взрослый человек")
else:
    print("Вы пенсионер")