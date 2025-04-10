
# Simulate rolling two dice, and prints results of each roll as well as the total.

# Solution: 

# Import the random library which lets us simulate random things like dice!
import random

def main():
    # Setting a seed is useful for debugging 
    # random.seed(1) 
    
    # Roll die
    die1: int = random.randint(1, 6)  # Number of sides on each die to roll
    die2: int = random.randint(1, 6)
    
    # Get their total
    total: int = die1 + die2
    
    # Print out the results
    print("Each Dice have 6 sides.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")

if __name__ == '__main__':
    main()

