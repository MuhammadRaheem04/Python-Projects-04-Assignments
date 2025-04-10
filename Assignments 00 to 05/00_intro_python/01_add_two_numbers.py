
# Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

# 1.Prompt the user to enter the first number.

# 2.Read the input and convert it to an integer.

# 3.Prompt the user to enter the second number.

# 4.Read the input and convert it to an integer.

# 5.Calculate the sum of the two numbers.

# 6.Print the total sum with an appropriate message.

# Solution:

def main():
    print("This program adds two numbers.") 
    while True:
          try:
                num1 : str = input("Enter first number: ") # gets 1st input number from the user in the form of string
                num1 : int = int(num1)   # change the type of input from string to nuber
                break
          except ValueError:
                print("Invalid input! Please enter a numeric value.")
    while True:
          try:
                num2  : str = input("Enter second number: ")   # gets 2nd input number from the user in the form of string
                num2 : int = int(num2)   # change the type of input from string to nuber
                break
          except ValueError:
                print("Invalid input! Please enter a numeric value.")
    
    total : int = num1 + num2  # sum the number 1 and number 2 
    print(f"{num1} + {num2} = {total}.")  # print the total 

    # print("The total is " + str(total) + ".") also we can write like this.

if __name__ == '__main__':
        main()