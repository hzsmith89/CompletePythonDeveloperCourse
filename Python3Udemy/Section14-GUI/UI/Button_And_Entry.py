from tkinter import *
from tkinter import ttk

root = Tk()

entry = ttk.Entry(root, width=30)
entry.pack()

button = ttk.Button(root, text="Click Me!")
button.pack()


def bu_click():
    print(entry.get())
    entry.delete(0, END)
    entry.insert(0, "button clicked!!")


button.config(command=bu_click)

root.mainloop()
