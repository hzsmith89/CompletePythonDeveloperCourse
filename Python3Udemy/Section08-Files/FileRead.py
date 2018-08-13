
def main():

    try:
        read_file = open("test.txt", "r")

        for line in read_file:
            print(line)

        read_file.close()
    except IOError:
        print("File not Found :(")

    finally:
        print("Done...")


if __name__ == '__main__':
    main()
