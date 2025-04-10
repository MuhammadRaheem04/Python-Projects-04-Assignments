#  Problem Statement

"""
Guess My Number

I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

Enter a new number: 25 Your guess is too low

Enter a new number: 40 Your guess is too low

Enter a new number: 45 Your guess is too low

Enter a new number: 48 Congrats! The number was: 48
"""

# solution 

import random 

def main():
  guess = random.randint(1, 99)
  while True:
    try:
      user_input: int = int(input("I am thinking of a number between 0 and 99... Enter a guess: "))
      if user_input < guess:
        print("Your guess is too low")
      elif user_input > guess:
        print("Your guess is too high")
      else:
        print(f"Congrats! The number was: {guess}")
        break
    except ValueError:
      print("Invalid input. Please enter a number.")

if __name__ == "__main__":
  main()
