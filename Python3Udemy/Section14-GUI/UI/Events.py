from tkinter import *
from tkinter import ttk

root = Tk()


def copy_press(event):
    print("type: {}".format(event.type))


def button_press(event):
    print("Button was pressed")


button = ttk.Button(root, text="Click Me!", width=25)
button.pack()
button.bind("<ButtonPress>", button_press)

root.bind("<Control-c>", copy_press)


root.mainloop()
