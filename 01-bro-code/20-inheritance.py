class Organism:
    alive = True


class Animal(Organism):
    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


class Prey:
    def flee(self):
        print("This animal flees")


class Predator:
    def hunt(self):
        print("This animal is hunting")


class Rabbit(Animal, Prey):  # multiple inheritance
    def run(self):
        print("This rabbit is running")

    def eat(self):  # method overriding
        print("This rabbit is eating")


class Fish(Animal, Prey, Predator):  # multiple inheritance
    def swim(self):
        print("This fish is swimming")


class Hawk(Animal, Predator):  # multiple inheritance
    def fly(self):
        print("This hawk is flying")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()

rabbit.flee()
fish.hunt()
fish.flee()
hawk.hunt()
