from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.title("Log In")
root.resizable = (False, False)  # Not Working

l1 = ttk.Label(root, text="Username:")
l1.grid(row=0, column=0)
et_username = ttk.Entry(root, width=20)
et_username.grid(row=0, column=1)
l2 = ttk.Label(root, text="Password:")
l2.grid(row=1, column=0)
et_password = ttk.Entry(root, width=20, show="*")
et_password.grid(row=1, column=1)
login_button = ttk.Button(root, text="Log In")
login_button.grid(row=2, column=1)


def but_click():
    print("Username: {} Password: {}".format(et_username.get(), et_password.get()))

    if et_username.get() == "admin" and et_password.get() == "1234":
        messagebox.showinfo("Login Info", "Welcome to the Python App")
    else:
        messagebox.showerror("Login Info", "Login Failed! \nUsername and password not recognized.")


login_button.config(command=but_click)

root.mainloop()
