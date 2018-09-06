from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DB_Handler import DBHandler


class ListTickets:

    def __init__(self):
        self._db_handler = DBHandler()
        self._root = Tk()

        tree_view = ttk.Treeview(self._root)
        tree_view.pack()
        tree_view.heading("#0", text="ID")
        tree_view.configure(column=("Name", "Gender", "Comment"))
        tree_view.heading("Name", text="Name")
        tree_view.heading("Gender", text="Gender")
        tree_view.heading("Comment", text="Comment")
        cursor = self._db_handler.list_tickets()

        for row in cursor:
            tree_view.insert("", "end", "#{}".format(row["ID"]), text=row["ID"])
            tree_view.set("#{}".format(row["ID"]), "Name", row["Name"])
            tree_view.set("#{}".format(row["ID"]), "Gender", row["Gender"])
            tree_view.set("#{}".format(row["ID"]), "Comment", row["Comment"])
            # print("ID: {}, Name: {}, Gender: {}, Comment: {}".format(row["ID"], row["Name"],
            #                                                            row["Gender"], row["Comment"]))

        self._root.mainloop()
