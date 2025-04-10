
# Write a function that takes two numbers and finds the average between the two.

# Solution 


def find_average(num1: float, num2: float):
    """
    Returns the number which is half way between a and b
    """
    return (num1 + num2) / 2  # Sum both numbers and divide by 2

def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    average = find_average(num1,num2)
   
    print(f"The Average of {num1} and {num2} is: {average}")
    

if __name__ == '__main__':
    main()