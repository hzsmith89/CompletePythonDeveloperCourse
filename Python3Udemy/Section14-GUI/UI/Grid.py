from tkinter import *
from tkinter import ttk

root = Tk()

# Style Sheet
style = ttk.Style()
# theme_use allows background color to be used
style.theme_use('classic')
# creates a style for all labels
style.configure('TLabel', foreground="Black")

# Label Creation
# pad == padding outside of object
ttk.Label(root, text="Green", background="Green").grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
# ipad == padding inside of object
ttk.Label(root, text="Yellow", background="Yellow").grid(row=0, column=1, ipadx=5, ipady=5, sticky="nsew")
# sticky spans the entire background
ttk.Label(root, text="Blue", background="Blue").grid(row=0, rowspan=2, column=2, sticky="ns")
ttk.Label(root, text="Red", background="Red").grid(row=1, column=0, columnspan=2, sticky='ew')

# Configures the rows to keep consistent on screen size
root.rowconfigure(0, weight=2)
root.rowconfigure(1, weight=1)

root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=2)


root.mainloop()
