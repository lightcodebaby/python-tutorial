class Car:

    wheels = 4  # class variable

    def __init__(self, make, model, year, color):  # instance variables
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This " + self.model + " is driving")

    def stop(self):
        print("This " + self.model + " is stopped")
