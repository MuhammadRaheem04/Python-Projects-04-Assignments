
"""
Problem Statement
Fill out the subtract_seven helper function to subtract 7 from num, and fill out the main() method to call the subtract_seven helper function! If you're stuck, revisit the add_five example from lecture.
"""

# Solution 

def main():
    num: int = 7
    num = subtract_seven(num)
    print("this should be zero:", num)
    
    num2: int = 15
    num2 = subtract_seven(num2)  # 15 - 7 = 8
    print("The result after subtracting 7 is:", num2)  

def subtract_seven(num):
    num = num - 7
    return num

if __name__ == '__main__':
    main()
