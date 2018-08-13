from Class_DB_Connect import DBConnect


def main():
    db_connect = DBConnect()

    while True:
        index_option = int(input("Select number for operation"
                                 "\n1: Add Record \n2: List Admins "
                                 "\n3: Update Record \n4: Delete Record "
                                 "\n0: Quit \nOption: "))
        print()

        if index_option == 1:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            db_connect.add(name, age)

        elif index_option == 2:
            db_connect.list_admins()

        elif index_option == 3:
            id = int(input("Enter ID: "))
            name = input("Enter New Name: ")
            age = int(input("Enter New Age: "))
            db_connect.update_record(id, name, age)

        elif index_option == 4:
            id = int(input("Enter ID to Delete: "))
            db_connect.delete_record(id)

        elif index_option == 0:
            print("Goodbye...")
            break

        else:
            print("Invalid option!! \nYou Suck")

        print()


if __name__ == '__main__':
    main()