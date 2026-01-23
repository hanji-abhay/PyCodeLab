# Number Guessing Game
# The computer chooses a number, and the player tries to guess it

import random

# Generate a random number between 1 and 50
number_to_guess = random.randint(1, 50)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 50")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")
        break
