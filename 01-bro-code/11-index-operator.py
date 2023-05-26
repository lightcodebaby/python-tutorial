name = "ruben lopez!"

if name[0].islower():
    name = name.capitalize()

print(name)  # Ruben Lopez

first_name = name[:5].upper()
last_name = name[6:].lower()
last_character = name[-1]

print(first_name)  # RUBEN
print(last_name)  # lopez
print(last_character)
