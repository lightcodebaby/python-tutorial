import time

# While loop

name = ""
last_name = None

while len(name) == 0 or not last_name:
    name = input("Enter your name: ")
    last_name = input("Enter your last name")

print("Hello " + name + " " + last_name)

# For loop

for i in range(10):
    print(i)  # 0, ..., 9

for i in range(50, 100):
    print(i)  # 50, ..., 99

for i in range(50, 100, 2):
    print(i)  # 50, 52, 54, ..., 96, 98

for i in "Ruben Lopez Gomez":
    print(i)

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)

print("It's the final countdown!")

# Nested loop

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

# Control statements

while True:
    name = input("Enter your name: ")
    if name != "":
        break

number = "123-456-7890"

for i in number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1, 21):
    if i == 13:
        pass
    print(i)
