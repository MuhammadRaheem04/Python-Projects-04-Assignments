
# Write a program that asks a user to enter a number. Your program will then double that number and print out the result. It will repeat that process until the value is 100 or greater.

# For example if the user enters the number 2 you would then print:

# 4 8 16 32 64 128

# Solution:

def main():
    curr_value = int(input("Enter a number: "))  # Ask user for a number
    
    while curr_value <= 100:  # Continue doubling while value is less than or equal to 100
        curr_value *= 2  # Double the current value
        print(curr_value, end=" ")  # Print on the same line with space

if __name__ == "__main__":
    main()

