from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DB_Handler import DBHandler
from List_Reservation import ListTickets

db_handler = DBHandler()

root = Tk()
root.title("Ticket Reservation")
root.configure(background="#E1D8B2")

# Style
style = ttk.Style()
style.theme_use("classic")
style.configure("TLabel", background="#E1D8B2")
style.configure("TButton", background="#E1D8B2")
style.configure("TRadiobutton", background="#E1D8B2")

ttk.Label(root, text="Full Name").grid(row=0, column=0, pady=10, padx=10)
full_name_entry = ttk.Entry(root, width=30, font=("Arial", 16))
full_name_entry.grid(row=0, column=1, columnspan=2, pady=10)

ttk.Label(root, text="Gender").grid(row=1, column=0)
span_gender = StringVar()
span_gender.set("Male")
ttk.Radiobutton(root, text="Male", variable=span_gender, value="Male").grid(row=1, column=1)
ttk.Radiobutton(root, text="Female", variable=span_gender, value="Female").grid(row=1, column=2)

ttk.Label(root, text="Comments").grid(row=2, column=0, pady=10)
comment_text = Text(root, width=30, height=15, font=("Arial", 16))
comment_text.grid(row=2, column=1, columnspan=2, pady=10)

ttk.Button(root, text="Submit", command=lambda: button_click()).grid(row=3, column=3, pady=10)
ttk.Button(root, text="List All", command=lambda: list_all_click()).grid(row=3, column=2, pady=10)


def button_click():
    print("Full Name: {}".format(full_name_entry.get()))
    print("Gender: {}".format(span_gender.get()))
    print("Comments: {}".format(comment_text.get(1.0, "end")))

    message = db_handler.add(full_name_entry.get(), span_gender.get(), comment_text.get(1.0, "end"))
    messagebox.showinfo(title="Add Info", message=message)

    full_name_entry.delete(0, "end")
    comment_text.delete(1.0, "end")


def list_all_click():
    ListTickets()


root.mainloop()

