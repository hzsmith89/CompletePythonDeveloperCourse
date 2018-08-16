from tkinter import *
from tkinter import ttk

# Instantiates GUI Window
root = Tk()

# Creates Buttons
button1 = ttk.Button(root, text="Button 1")
button1.pack()
button2 = ttk.Button(root, text="Button 2")
button2.pack()
button3 = ttk.Button(root, text="Button 3")
button3.pack()

# Instantiates Style Object
style = ttk.Style()

# Prints Theme List ('aqua', 'clam', 'alt', 'default', 'classic')
style.theme_names()

# Prints Current Theme
style.theme_use()

# Changes Theme
style.theme_use('alt')
style.theme_use('clam')
style.theme_use('default')
style.theme_use('classic')
style.theme_use('aqua')

# Changes All Button Foregrounds to Red
style.configure('TButton', foreground='red')

# Prints class of Button ig: 'TButton'
button1.winfo_class()

# Changes Style for all Buttons
style.configure('TButton', foreground='red', font=('Arial', 24))

# Creates Class For All Buttons
style.configure('Info.TButton', foreground='blue', font=('Arial', 18, 'bold'))

# Adds Custom Class To Button 3
button3.configure(style='Info.TButton')

# Maps know style guides to Info Style Class
style.map('Info.TButton', background=[('pressed', 'blue'),('disabled', 'grey')])

# Disables Button 2
button2.state(['disabled'])

# Enables Button 2
button2.state(['!disabled'])
