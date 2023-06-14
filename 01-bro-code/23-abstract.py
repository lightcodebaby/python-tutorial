from abc import ABC, abstractmethod


class Vehicle:
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")


class Motorcycle(Vehicle):
    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("You stop the motorcycle")


# vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()
