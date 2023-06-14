friends = [
    ("Rachel", 19),
    ("Monica", 18),
    ("Phoebe", 17),
    ("Joey", 16),
    ("Chandler", 21),
    ("Ross", 20),
]

check_age = lambda data: data[1] >= 18

older_than_eighteen = filter(check_age, friends)

for friend in older_than_eighteen:
    print(friend)
