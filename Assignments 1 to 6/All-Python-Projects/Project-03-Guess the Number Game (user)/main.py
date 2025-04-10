
import random

print("Welcome to the Number Guessing Game!")
print("I will think of a number between 1 and 10, and you have to guess it.")

secret_num = random.randint(1, 10)
print("I have a secret number between 1 and 10. Can you guess it?")

while True:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number only.")
        continue

    if guess < 1 or guess > 10:
        print("Your guess is out of range! Please guess a number between 1 and 10.")
    elif guess < secret_num:
        print("Too low! Try again.")
    elif guess > secret_num:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        break