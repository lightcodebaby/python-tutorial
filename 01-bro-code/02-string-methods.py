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
