
"""
Problem Statement
Write a function called print_ones_digit , which takes as a parameter an integer num and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here. Call your function from main()!

Here's a sample run:

Enter a number: 42 The ones digit is 2
"""

# Solution 

def print_ones_digit(num):
    print("The ones digit is", num % 10)

def main():
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
            
    print_ones_digit(num)

if __name__ == '__main__':
    main()