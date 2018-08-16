from tkinter import *
from tkinter import ttk


def button_click(id_number):
    print("Id:{}".format(id_number))


root = Tk()

ttk.Button(root, width=25, text="Click Me 1", command=lambda: button_click(1342)).pack()

root.mainloop()
