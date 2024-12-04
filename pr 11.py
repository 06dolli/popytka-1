import tkinter as tk
from tkinter import ttk, messagebox, filedialog

def create_calculator(tab):
    num1 = tk.Entry(tab)
    num2 = tk.Entry(tab)
    operation = ttk.Combobox(tab, values=['+', '-', '*', '/'])
    operation.current(0)
    result = tk.Label(tab, text="Результат: ")

    num1.pack(pady=10)
    operation.pack(pady=10)
    num2.pack(pady=10)
    btn_calculate = tk.Button(tab, text="Посчитать", command=calculate(num1, num2, operation, result))
    btn_calculate.pack(pady=10)
    result.pack(pady=10)

def calculate(num1, num2, operation, result):
    try:
        n1 = float(num1.get())
        n2 = float(num2.get())
        op = operation.get()
        if op == '+':
            res = n1 + n2
        elif op == '-':
            res = n1 - n2
        elif op == '*':
            res = n1 * n2
        elif op == '/':
            res = n1 / n2
        result.config(text=f"Результат: {res}")
    except ValueError:
        messagebox.showerror("Ошибка", "Пожалуйста, введите числа.")

def create_checkboxes(tab):
    choice1 = tk.IntVar()
    choice2 = tk.IntVar()
    choice3 = tk.IntVar()

    chk1 = tk.Checkbutton(tab, text="Первый", variable=choice1)
    chk2 = tk.Checkbutton(tab, text="Второй", variable=choice2)
    chk3 = tk.Checkbutton(tab, text="Третий", variable=choice3)

    chk1.pack(pady=5)
    chk2.pack(pady=5)
    chk3.pack(pady=5)

    btn_show_choice = tk.Button(tab, text="Показать выбор", command=show_choice(choice1, choice2, choice3))
    btn_show_choice.pack(pady=10)

def show_choice(choice1, choice2, choice3):
    choices = []
    if choice1.get():
        choices.append("первый вариант")
    if choice2.get():
        choices.append("второй вариант")
    if choice3.get():
        choices.append("третий вариант")
    if choices:
        messagebox.showinfo("Ваш выбор", f"Вы выбрали: {', '.join(choices)}")
    else:
        messagebox.showinfo("Ваш выбор", "Вы ничего не выбрали.")

def create_text_file_loader(tab):
    text_area = tk.Text(tab, wrap=tk.WORD)
    text_area.pack(expand=True, fill='both', padx=10, pady=10)
    
    btn_load_file = ttk.Button(tab, text="Загрузить текстовый файл", command=load_file(text_area))
    btn_load_file.pack(pady=10)

def load_file(text_area):
    file_path = filedialog.askopenfilename(filetypes=[("Текстовые файлы", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            text_area.delete(1.0, tk.END)  # Очистка текстового поля
            text_area.insert(tk.END, content)  # Вставка содержимого файла

# Главная часть программы
root = tk.Tk()
root.title("Кушлакова Дарья Альбертова")
root.geometry("666*999")

# Создание вкладок
tabs = ttk.Notebook(root)
tab1 = ttk.Frame(tabs)
tab2 = ttk.Frame(tabs)
tab3 = ttk.Frame(tabs)

tabs.add(tab1, text='Калькулятор')
tabs.add(tab2, text='Чекбоксы')
tabs.add(tab3, text='Работа с текстом')

tabs.pack(expand=1, fill='both')

create_calculator(tab1)
create_checkboxes(tab2)
create_text_file_loader(tab3)

root.mainloop()