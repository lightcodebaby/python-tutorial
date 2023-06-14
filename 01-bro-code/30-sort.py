letters = ["R", "L", "G", "P", "A", "M"]

sorted_letters = sorted(letters, reverse=True)
for letter in sorted_letters:
    print(letter)

letters.sort(reverse=True)
for letter in letters:
    print(letter)

family = [
    ("Ruben", "RLG", 29),
    ("Peter", "P", 5),
    ("Aegon", "A", 5),
    ("Mom", "MSGF", 58),
]

family.sort()  # first column

initial = lambda initials: initials[1]

family.sort(key=initial, reverse=True)
print(family)

# to use sorted function

family = (
    ("Ruben", "RLG", 29),
    ("Peter", "P", 5),
    ("Aegon", "A", 5),
    ("Mom", "MSGF", 58),
)

initial = lambda initials: initials[1]
sorted_family = sorted(family, key=initial)
print(sorted_family)
