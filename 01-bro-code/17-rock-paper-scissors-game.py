import random

choices = ["rock", "paper", "scissors"]

while True:
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors?: ").lower()

    print("computer: " + computer)
    print("player: " + player)

    if player == computer:
        print("Tie!")
    elif (
        (player == "rock" and computer == "scissors")
        or (player == "paper" and computer == "rock")
        or (player == "scissors" and computer == "paper")
    ):
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Bye!")
