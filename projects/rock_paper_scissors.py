# Rock Paper Scissors Game
# User plays against the computer

import random

options = ["rock", "paper", "scissors"]

print("Welcome to Rock Paper Scissors Game!")

while True:
    user_choice = input("Enter rock, paper, scissors (or 'quit' to exit): ").lower()
    if user_choice == "quit":
        print("Thanks for playing!")
        break
    if user_choice not in options:
        print("Invalid choice, try again!")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win! 🎉")
    else:
        print("You lose! 😢")
