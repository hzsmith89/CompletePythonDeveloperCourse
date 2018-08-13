class Car:

    def __init__(self, type, model, price, miles_drive, owner):
        self.type = type
        self.model = model
        self.price = price
        self.miles_drive = miles_drive
        self.owner = owner

    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def set_miles_drive(self, miles_drive):
        self.miles_drive= miles_drive

    def get_miles_drive(self):
        return self.miles_drive

    def set_owner(self, owner):
        self.owner = owner

    def get_owner(self):
        return self.owner

    def get_current_price(self):
        return self.price - (self.miles_drive * 10)


def main():
    my_car = Car("VW", "Camper", 60000, 5000, "Halsey Smith")
    print("New price: ${}".format(my_car.get_current_price()))

    alex_car = Car("Aston Martin", "Vanquish", 100000, 3000, "James Bond")
    current_price = alex_car.get_current_price()
    print(current_price)


if __name__ == '__main__':
    main()
