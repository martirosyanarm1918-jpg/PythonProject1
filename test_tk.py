from tkinter import *
root = Tk()

#окно
root['bg'] = 'green'
root.title('name_programme')
root.geometry('300x300')

#меню
menu_bar = Menu(root)

file_menu = Menu(menu_bar, tearoff = 0)
file_menu.add_command()
root.mainloop()

