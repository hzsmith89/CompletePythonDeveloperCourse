
def main():
    try:
        out = open("test.txt", "a")

        for i in range(5):
            line = input("Enter line to write: ")
            out.write(line)
            out.write("\n")
        out.close()

    except IOError:
        print("File not Found :(")

    finally:
        print("App is done writing.")


if __name__ == '__main__':
    main()
