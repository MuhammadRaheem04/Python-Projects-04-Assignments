
import random

print("Welcome to the Number Guessing Game! ")

low = 1
high = 10

print ("Think of a number between 1 and 10. and Computer will guess it.")

if low <= high:
    guess = random.randint(low, high)
    print(f"Computer guessed: {guess}")

    while True:
        feedback = input("If the guess is too high type (H), too low type (L), or correct type (C)? ").strip().upper()

        if feedback == 'H':
            high = guess - 1
            guess = random.randint(low, high)
            print(f"Computer guessed: {guess}")
        elif feedback == 'L':
            low = guess + 1
            guess = random.randint(low, high)
            print(f"Computer guessed: {guess}")
        elif feedback == 'C':
            print("Computer guessed it right!")
            break
        else:
            print("Invalid input. Please enter H, L, or C.")
    if low > high:
        print("Invalid range. Please ensure that low is less than or equal to high.")