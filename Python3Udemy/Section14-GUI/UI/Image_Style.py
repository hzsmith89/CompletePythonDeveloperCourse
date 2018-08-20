from tkinter import *
from tkinter import ttk

root = Tk()

style = ttk.Style()
style.configure('TButton', foreground='red', font=('Arial', 18))

entry = ttk.Entry(root, width=30)
entry.pack()

button = ttk.Button(root, text="Click Me!")
button.pack()
logo = PhotoImage(file="logo.gif")
button.config(image=logo, compound=LEFT)
resize_logo = logo.subsample(10, 10)
button.config(image=resize_logo)


def bu_click():
    print(entry.get())
    entry.delete(0, END)
    entry.insert(0, "button clicked!!")


button.config(command=bu_click)

root.mainloop()
