
# Write a program that prints the first 20 even numbers. There are several correct approaches, but they all use a loop of some sort. Do no write twenty print statements

# The first even number is 0:

# 0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38

# Solution 01:

def main():
    # This for-loop start at 0 and counts up to 19 (for a total of 20 numbers)
    for i in range(20):
        print(i * 2, end=" ")  # Use the 'i' value inside the for-loop and multiply with 2 to get even number only
   
# Call the main function
if __name__ == "__main__":
    main()

print()  # Print a new line after the loop

# Solution 02:
def main():
    # This for-loop start at 0 and counts up to 39 (for a total of 40 numbers)
    for i in range(40):
        if i % 2 == 0:  # Check if the number is even
            print(i, end=" ")  # Print the even number

if __name__ == "__main__":
    main()  # Call the main function


print()  # Print a new line after the loop


# Solution 03:
def main():
    for i in range(0, 39, 2):
        # This for-loop start at 0 and counts up to 39 (for a total of 40 numbers) with a step of 2
        # The step of 2 ensures that only even numbers are printed
        print(i, end=" ")

if __name__ == "__main__":
    main()  # Call the main function
