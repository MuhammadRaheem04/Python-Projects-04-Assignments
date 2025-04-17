
"""
Problem Statement
10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd
"""

# Solution 

def main():
    for i in range(10, 20):
        if is_odd(i):
            print(f'{i} odd ', end=' ')
        else:
            print(f'{i} even ', end=' ')
            
def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns true.
    """
    
    remainder = value % 2  # 0 if value is divisible by 2, 1 if it isn't
    return remainder == 1

if __name__ == '__main__':
    main()


# Solution 02 

def even_or_odd():
    for num in range(10, 20):  # from 10 to 19 inclusive
        if num % 2 == 0:
            print(f"{num} even", end=" ")
        else:
            print(f"{num} odd", end=" ")

def main():
    even_or_odd()

if __name__ == "__main__":
    main()
