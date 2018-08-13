class Car:

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
    my_car = Car()
    my_car.set_type("VW")
    my_car.set_model("Camper")
    my_car.set_price(60000)
    my_car.set_miles_drive(5000)
    my_car.set_owner("Halsey Smith")

    print("New price: ${}".format(my_car.get_current_price()))

    alex_car = Car()
    alex_car.set_type("Aston Martin")
    alex_car.set_model("Vanquish")
    alex_car.set_price(100000)
    alex_car.set_miles_drive(3000)
    alex_car.set_owner("James Bond")
    current_price = alex_car.get_current_price()
    print(current_price)


if __name__ == '__main__':
    main()
