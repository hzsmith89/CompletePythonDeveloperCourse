import sqlite3


class DBConnect:

    def __init__(self):
        self.db = sqlite3.connect("Information.db")
        self.db.row_factory = sqlite3.Row
        self.db.execute("create TABLE if not exists Admin(ID integer primary key autoincrement, Name text, Age int)")
        self.db.commit()

    def add(self, name, age):
        self.db.execute("INSERT into Admin(Name, Age) values(?, ?)", (name, age))
        self.db.commit()
        print("Record Added.")

    def list_admins(self):
        cursor = self.db.execute("SELECT * FROM Admin")
        for row in cursor:
            print("ID: {}, Name: {}, Age: {}".format(row["ID"], row["Name"], row["Age"]))

    def delete_record(self, id):
        self.db.execute("DELETE from Admin WHERE ID={}".format(id))
        self.db.commit()
        print("Record Deleted.")

    def update_record(self, id, name, age):
        self.db.execute("UPDATE Admin set Name=?, Age=? WHERE ID=?", (name, age, id))
        self.db.commit()
        print("Record Updated.")
