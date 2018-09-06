import sqlite3


class DBHandler:

    def __init__(self):
        self._db = sqlite3.connect("Reservation.db")
        self._db.row_factory = sqlite3.Row
        self._db.execute("create TABLE if not exists Ticket(ID integer primary key autoincrement, "
                         "Name text, Gender int, Comment text)")
        self._db.commit()

    def add(self, name, gender, comment):
        self._db.execute("INSERT into Ticket(Name, Gender, Comment) values(?, ?, ?)", (name, gender, comment))
        self._db.commit()
        return "Ticket Added."

    def list_tickets(self):
        return self._db.execute("SELECT * FROM Ticket")

    def update_record(self, id, name, gender, comment):
        self._db.execute("UPDATE Ticket set Name=?, Age=?, Comment=? WHERE ID=?", (name, gender, comment, id))
        self._db.commit()
        return "Ticket Updated."

    def delete_record(self, id):
        self._db.execute("DELETE from Ticket WHERE ID={}".format(id))
        self._db.commit()
        return "Ticket Deleted."




