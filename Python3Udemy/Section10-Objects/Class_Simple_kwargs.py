class Car:

    def __init__(self, **kwargs):
        self.data = kwargs

    def get_type(self):
        return self.data["Type"]

    def get_model(self):
        return self.data["Model"]

    def get_price(self):
        return self.data["Price"]

    def get_miles_drive(self):
        return self.data["Miles_Drive"]

    def get_owner(self):
        return self.data["Owner"]

    def get_current_price(self):
        return self.get_price() - (self.get_miles_drive() * 10)


def main():
    my_car = Car(Type="VW", Model="Camper", Price=60000, Miles_Drive=5000, Owner="Halsey Smith")
    print("My Car's New Price: ${}".format(my_car.get_current_price()))

    james_car = Car(Type="Aston Martin", Model="Vanquish", Price=100000, Miles_Drive=3000, Owner="James Bond")
    print("007's New Price: ${}".format(james_car.get_current_price()))

    tim_car = Car(Price=5000, Miles_Drive=200)
    print("Tim's New Price: ${}".format(tim_car.get_current_price()))


if __name__ == '__main__':
    main()
