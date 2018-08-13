class User:

    def __init__(self, name, age):
        print("Great Object")
        self.name = name
        self.age = age

    def set_name(self, name, age):
        self.name = name

    def get_name(self):
        return self.name

    def set_age(self, age):
        self.age = age

    def get_age(self):
        return self.age


def main():
    u1 = User("tom pickles", 24)
    print("Name: {} Age:{}".format(u1.get_name(), u1.get_age()))

    u2 = User("chuck finnster", 25)
    print("Name: {} Age:{}".format(u2.get_name(), u2.get_age()))


if __name__ == '__main__':
    main()
