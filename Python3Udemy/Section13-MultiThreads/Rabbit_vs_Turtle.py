import time
import _thread
race_length = 100
winner = False


class Animal:

    def __init__(self, name, speed, rest_time):
        self.name = name
        self.speed = speed
        self.rest_time = rest_time
        self.distance = 0

    def get_name(self):
        return self.name

    def get_rest_time(self):
        return self.rest_time

    def get_speed(self):
        return self.speed

    def get_distance(self):
        return self.distance

    def run(self):
        global race_length
        global winner

        while self.get_distance() < race_length and not winner:
            self.distance = self.get_distance() + self.get_speed()
            print("{} ran {} meters. Is now at {} meters.".format(self.get_name(), self.get_speed(), self.get_distance()))

            if self.get_distance() >= race_length:
                winner = True
                print_winner(self)

            else:
                self.rest()

    def rest(self):
        # print("{} is now resting for {} seconds.".format(self.get_name(), self.get_rest_time()))
        time.sleep(self.get_rest_time())

    def __str__(self):
        return "[Name: {}, Speed: {}, Rest Time: {}]".format(self.get_name(), self.get_speed(), self.get_rest_time())

def print_winner(race_winner):
    print()
    print("{} has won the race!!".format(race_winner.get_name()))
    print()

def race_start():
    print("On your mark...")
    time.sleep(1)
    print("Get set...")
    time.sleep(1)
    print("GO!!!")
    print()


def print_racers(racers):

    for racer in racers:
        print(racer)

    print()

def print_final_distances(racers):
    for racer in racers:
        print("{} finshed at {}.".format(racer.get_name(), racer.get_distance()))
    print()

def main():
    rabbit = Animal("Peter", 25, 3)
    turtle = Animal("Myrtle", 15, 1)
    penguin = Animal("Tux", 20, 2)

    print_racers([rabbit, turtle, penguin])

    race_start()

    _thread.start_new_thread(rabbit.run, (), )
    _thread.start_new_thread(turtle.run, (), )
    _thread.start_new_thread(penguin.run, (), )

    while not winner:
        pass

    print_final_distances([rabbit, turtle, penguin])

if __name__ == "__main__":
    main()
