
"""
Problem Statement
Implement the following function which takes in 3 integers as parameters:

def in_range(n, low, high) Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """

# Solution 

def in_range(n, low, high):

    if n >= low and n <= high:
        return True
    # we could have also included an else statement, but since we are returning, it's fine without!
    return False

def main():
    # Test cases
    print(in_range(5, 1, 10))   # True (5 is within the range)
    print(in_range(1, 1, 10))   # True (1 is exactly at the lower boundary)
    print(in_range(10, 1, 10))  # True (10 is exactly at the upper boundary)
    print(in_range(0, 1, 10))   # False (0 is less than the range)
    print(in_range(11, 1, 10))  # False (11 is greater than the range)

if __name__ == "__main__":
    main()