# This project was made in the terminal some comment below dictate what happened when selecting buttons and boxes

from tkinter import *
from tkinter import ttk

root = Tk()
cb = ttk.Checkbutton(root, text="Is married")
cb.pack()

# State for Checkbox
state = StringVar()
state.set("yes")
state.get()  # displayed'yes'

cb.config(variable=state, onvalue="Yes married", offvalue="No not married")

state.get()  # displayed 'Yes married' after selecting checkbox
state.get()  # displayed 'No not married' after unselecting checkbox

# state for radio buttons
rb_var = StringVar()

rb1 = ttk.Radiobutton(root, text="Male", variable=rb_var, value="is male")
rb1.pack()

rb_var.get()  # displayed 'is male' after radio button selection

rb2 = ttk.Radiobutton(root, text="Female", variable=rb_var, value="is female")
rb2.pack()

rb_var.get()  # displayed 'is female' after radio button selection
rb_var.get()  # displayed 'is male' after radio button selection
