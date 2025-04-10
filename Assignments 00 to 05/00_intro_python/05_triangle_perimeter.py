
# Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

# Here's a sample run of the program (user input is in bold italics):

# What is the length of side 1? 3

# What is the length of side 2? 4

# What is the length of side 3? 5.5

# The perimeter of the triangle is 12.5

from math import e


def main():
    while True:
        try:
            # Get the 3 side lengths of the triangle
            side1: float = float(input("What is the length of side 1 of the triangle? "))
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
    while True:
        try:
            side2: float = float(input("What is the length of side 2 of the triangle? "))
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
    while True:
        try:
            side3: float = float(input("What is the length of side 3 of the triangle? "))
            break
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
    # Print out the perimeter (sum of the sides) of the triangle, make sure to cast it to a str when concatenating!
    print(f"The perimeter of the triangle is {side1 + side2 + side3}")

if __name__ == '__main__':
    main()