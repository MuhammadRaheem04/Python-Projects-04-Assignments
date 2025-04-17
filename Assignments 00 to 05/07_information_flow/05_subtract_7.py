
"""
Problem Statement
Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.
"""

# Solution 

def subtract_seven(num):
    num = num - 7
    return num

def main():
    while True:
        try:
            num: int = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    result = subtract_seven(num)
    print("The result after subtracting 7 is:", result)

if __name__ == '__main__':
    main()
