print(happy := True)

foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)

# or...

foods = list()
while food := ("What food do you like?: ") != "quit":
    foods.append(food)
