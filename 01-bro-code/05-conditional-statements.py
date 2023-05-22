age = int(input("How old are you?: "))

if age > 18:
    print("You are an adult!")
elif age == 100:
    print("You are a centruy old!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are a child")

# Logical operators

temp = int(input("What is the temperature outside?: "))

if not (temp >= 0 and temp <= 30):
    print("Stay inside!")
elif not (temp < 0 or temp > 30):
    print("Go outside!")
