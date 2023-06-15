usernames = ["Ruben", "Peter", "Aegon", "Mom"]
passwords = ["p@ssword1", "p@ssword2", "p@ssword3", "p@ssword4"]
login_date = ["1/1/2023","1/4/2023","1/3/2023","1/2/2023"]

users = list(zip(usernames, passwords, login_date))

for user in users:
    print(user)
