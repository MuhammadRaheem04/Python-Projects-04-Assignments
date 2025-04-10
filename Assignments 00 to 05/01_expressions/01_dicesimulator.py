
# Simulate rolling two dice, three times. Prints the results of each die roll. This program is used to show how variable scope works.

# Solution:

# Import the random library which lets us simulate random things like dice!
import random

# Number of sides on each die to roll
NUM_SIDES = 6

def roll_dice():
    """
    Simulates rolling two dice and prints their total
    """
    die1: int = random.randint(1, NUM_SIDES)  # Generates a random number between 1 and 6
    die2: int = random.randint(1, NUM_SIDES)
    total: int = die1 + die2   # Calculates the sum of the two dice
    print("Total of two dice:", total)

def main():
    die1: int = 10    # Local variable 'die1' inside main()
    print("die1 in main() starts as: " + str(die1))   # Displays its initial value
    roll_dice()  # Calls roll_dice() (first roll)
    roll_dice()  # Calls roll_dice() (second roll)
    roll_dice()  # Calls roll_dice() (third roll)
    print("die1 in main() is: " + str(die1))  # After rolling, the program prints die1 in main() again to show that its value did not change despite roll_dice() also having a die1 variable.



if __name__ == '__main__':
    main()