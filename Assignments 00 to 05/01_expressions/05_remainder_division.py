
# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

# Here's a sample run of the program:

# Please enter an integer to be divided: 5

# Please enter an integer to divide by: 3

# The result of this division is 1 with a remainder of 2

# Solution: 

def main():
    while True:
        try:
            # Get the dividend from user input
            dividend: int = int(input("Please enter an integer to be divided: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    while True:
        try:
            # Get the divisor from user input
            divisor: int = int(input("Please enter an integer to divide by: "))
            if divisor == 0:
                print("Cannot divide by zero. Please enter a non-zero integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    quotient: int = dividend // divisor  # Divide with no remainder/decimals (integer division)
    remainder: int = dividend % divisor  # Get the remainder of the division (modulo)
    
    print(f"The result of this division is {quotient} with a remainder of {remainder}.")


if __name__ == '__main__':
    main()
