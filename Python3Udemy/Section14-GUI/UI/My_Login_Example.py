from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Log In")
root.resizable = (False, False)  # Not Working

input_frame = ttk.Frame(root)
input_frame.config(height=200, width=200, relief=RIDGE, padding=(10, 10))
input_frame.pack()

ttk.Label(input_frame, text="Username:").grid(row=0, column=0)
username_entry = ttk.Entry(input_frame)
username_entry.grid(row=0, column=1)

ttk.Label(input_frame, text="Password:").grid(row=1, column=0)
password_entry = ttk.Entry(input_frame, show="*")
password_entry.grid(row=1, column=1)


def log_in():
    print("Username: {}".format(username_entry.get()))
    username_entry.delete(0, END)
    print("Password: {}".format(password_entry.get()))
    password_entry.delete(0, END)


login_button = ttk.Button(input_frame, text="Log In", width=10, command=lambda: log_in())
login_button.grid(row=2, column=0, columnspan=2)

root.mainloop()
