import sqlite3
db = sqlite3.connect("Information.db")


def create_table():
    db.row_factory = sqlite3.Row
    db.execute("create TABLE if not exists Admin(ID integer primary key autoincrement, Name text, Age int)")
    db.commit()


def add(name, age):
    db.execute("INSERT into Admin(Name, Age) values(?, ?)", (name, age))
    db.commit()
    print("Record Added.")


def list_admins():
    cursor = db.execute("SELECT * FROM Admin")
    for row in cursor:
        print("ID: {}, Name: {}, Age: {}".format(row["ID"], row["Name"], row["Age"]))


def delete_record(id):
    db.execute("DELETE from Admin WHERE ID={}".format(id))
    db.commit()
    print("Record Deleted.")


def update_record(id, name, age):
    db.execute("UPDATE Admin set Name=?, Age=? WHERE ID=?", (name, age, id))
    db.commit()
    print("Record Updated.")


def main():
    create_table()

    while True:
        index_option = int(input("Select number for operation"
                                 "\n1: Add Record \n2: List Admins "
                                 "\n3: Update Record \n4: Delete Record "
                                 "\n0: Quit \nOption: "))
        print()

        if index_option == 1:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            add(name, age)

        elif index_option == 2:
            list_admins()

        elif index_option == 3:
            id = int(input("Enter ID: "))
            name = input("Enter New Name: ")
            age = int(input("Enter New Age: "))
            update_record(id, name, age)

        elif index_option == 4:
            id = int(input("Enter ID to Delete: "))
            delete_record(id)

        elif index_option == 0:
            print("Goodbye...")
            break

        else:
            print("Invalid option!! \nYou Suck")

        print()


if __name__ == '__main__':
    main()
