name = "Ruben lopez gomez"

# Basic methods

print(len(name))  # 5
print(name.find("u"))  # 1
print(name.capitalize())  # Ruben Lopez Gomez
print(name.upper())  # RUBEN LOPEZ GOMEZ
print(name.lower())  # ruben lopez gomez
print(name.isdigit())  # False
print(name.isalpha())  # False
print(name.count("o"))  # 2
print(name.replace(" ", ""))  # Rubenlopezgomez
print(name * 3)

# String slicing

name = "Ruben Lopez Gomez"

first_name = name[0:5]  # Ruben
last_name = name[6:17]  # Lopez Gomez
skipping_letters_name = name[0:17:2]  # RbnLpzGmz

# String reversing

reversed_name = name[::-1]

# Slice object

website = "https://google.com"
website2 = "https://wikipedia.com"

slice = slice(8, -4)

print(website[slice])  # google
print(website[slice])  # wikipedia

# String format

animal = "cow"
item = "moon"

print("The " + animal + " jumped over the " + item)
print("The {} jumped over the {}".format(animal, item))
print("The {1} jumped over the {0}".format(item, animal))
print("The {animal} jumped over the {item}".format(animal="cat", item="sun"))

text = "The {} jumped over the {}"
print(text.format(animal, item))

# Padding

name = "Ruben"

print(
    "Hello, my name is {:10}. Nice to meet you.".format(name)
)  # Hello, my name is Ruben     . Nice to meet you.
print(
    "Hello, my name is {:<10}. Nice to meet you.".format(name)
)  # Hello, my name is Ruben     . Nice to meet you.
print(
    "Hello, my name is {:>10}. Nice to meet you.".format(name)
)  # Hello, my name is      Ruben. Nice to meet you.
print(
    "Hello, my name is {:^10}. Nice to meet you.".format(name)
)  # Hello, my name is   Ruben   . Nice to meet you.

# Formatting numbers

number = 3.141519

print("The number pi is {:3f}".format(number))
print("The number pi is {:,}".format(number))
# print("The number pi is {0:b}".format(number))
# print("The number pi is {0:o}".format(number))
# print("The number pi is {0:X}".format(number))
# print("The number pi is {0:E}".format(number))
