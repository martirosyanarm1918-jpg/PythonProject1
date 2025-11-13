import secrets
import string
import tkinter as tk
from tkinter import messagebox

# Генерация пароля
def password_gen(complexity, length):
    if complexity == 'простой':
        characters = string.ascii_letters + string.digits
    elif complexity == 'сложный':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError("Выберите 'простой' или 'сложный'")
    return ''.join(secrets.choice(characters) for _ in range(length))

# Генерация и отображение пароля
def on_generate():
    complexity = complexity_var.get()
    try:
        length = int(length_entry.get())
        password = password_gen(complexity, length)
        result_var.set(password)
    except ValueError as e:
        messagebox.showerror("Ошибка", str(e))

# Копирование в буфер
def copy_to_clipboard():
    password = result_var.get()
    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        messagebox.showinfo("Скопировано", "Пароль скопирован в буфер обмена.")

# Интерфейс
window = tk.Tk()
window.title("SecureGen")
window.geometry("300x300")
window['bg'] = 'black'

tk.Label(window, text="Выберите сложность:").pack()
complexity_var = tk.StringVar(value="простой")
tk.Radiobutton(window, text="Простой", variable=complexity_var, value="простой").pack()
tk.Radiobutton(window, text="Сложный", variable=complexity_var, value="сложный").pack()

tk.Label(window, text="Введите длину пароля:").pack()
length_entry = tk.Entry(window)
length_entry.pack()

tk.Button(window, text="Создать пароль", command=on_generate).pack(pady=10)

# Результат — в Entry, чтобы можно было выделить и скопировать
result_var = tk.StringVar()
result_entry = tk.Entry(window, textvariable=result_var, width=40, justify='center')
result_entry.pack()

tk.Button(window, text="Скопировать", command=copy_to_clipboard).pack(pady=5)

#Сохранение генерации
#log.append(
#    'time': ...,
#     'length': ...,
#'password': ...
#)


window.mainloop()
#python main.py