import random

random_roll_dice = random.randint(1, 6)
print(random_roll_dice)

random_decimal_number = random.random()

options = ["rock", "paper", "scissors"]
random_play = random.choice(options)
print(random_play)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K"]
random.shuffle(cards)
print(cards)

