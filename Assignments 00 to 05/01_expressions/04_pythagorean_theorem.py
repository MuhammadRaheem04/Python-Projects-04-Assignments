
# Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

# It states that in a right triangle, the square of the hypotenuse is equal to the sum of the square of the other two sides.

# For instance, let's consider a right triangle ABC, with the right angle located at C. According to the Pythagorean theorem:

# BC ** 2 = AB ** 2 + AC ** 2

# Your code should read in the lengths of the sides AB and AC, and that outputs the length of the hypotenuse (BC). You will probably find math.sqrt() to be useful.

# Here's a sample run of the program (user input is in bold italics):

# Enter the length of AB: 3

# Enter the length of AC: 4

# The length of BC (the hypotenuse) is: 5.0


# Solution: 

import math

def main():
  while True:
    try:
      Side_AB: float = float(input("Enter the length of side AB: "))
      break
    except ValueError:
      print("Invalid input. Please enter a number.")
  while True:
    try:
      Side_AC: float = float(input("Enter the length of side AC: "))
      break
    except ValueError:
      print("Invalid input. Please enter a number.")
 
  Side_BC: float = (Side_AB ** 2 + Side_AC ** 2)
  result = math.sqrt(Side_BC)
  print(f"The length of side BC is: {result}")

if __name__ == "__main__":
  main()