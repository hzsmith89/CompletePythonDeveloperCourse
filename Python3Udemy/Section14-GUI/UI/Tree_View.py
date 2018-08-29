from tkinter import *
from tkinter import ttk

root = Tk()
tv=ttk.Treeview()
tv.pack()

# Insert into tree view (parent, index, id, text)
tv.insert("", "0", "item1", text="Halsey")
tv.insert("", "1", "item2", text="Kristofer")
tv.insert("", "0", "item3", text="Melissa")

# Move in tree view (id of item to move, parent, index under parent)
tv.move("item2", "item1", "0")
tv.move("item3", "item1", "0")

tv.insert("item1","0", "item4", text="Heather")
tv.insert("item1","0", "item5", text="Zack")

tv.move("item2", "item1", "3")
tv.move("item5", "item1", "2")

# Opens Branch
tv.item("item1", open=True)

# Removes item from parent but does not delete
tv.detach("item4")

# Moves Detached Item back into Parent
tv.move("item4", "item1", 0)

# Deletes Item from Tree View Permanently
tv.delete("item4")

tv.insert("item1", "0", "item4", text="Heather")

tv.delete("item5")

# Moves Items Under Parent
tv.move("item2", "", "end")
tv.move("item3", "", "0")
tv.move("item4", "", "0")

# Makes Second Column (Column Id)
tv.configure(column=("age"))

# Sets Column Width and Text Align (Column Id, width, text-align)
tv.column("age", width=20, anchor="center")
tv.column("age", width=60, anchor="center")
tv.column("#0", width=80, anchor="center")
tv.column("#0", width=100, anchor="center")

# Sets Column Heading (Column Id, Column Name)
tv.heading("#0", text="Name")
tv.heading("age", text="Age")

# Sets value in row and column (row item id, column id, value)
tv.set("item1", "age", "28")
tv.set("item1", "age", "29")
tv.set("item2", "age", "27")
tv.set("item3", "age", "45")
tv.set("item4", "age", "49")


# Prints tree view item on event click
def tv_select(event):
    print(tv.selection())


# Binds TreeviewSelect Event method to our treeview (Event Type, Method Name)
tv.bind("<<TreeviewSelect>>", tv_select)
