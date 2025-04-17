
"""
Problem Statement

Fill out the double(num) function to return the result of multiplying num by 2. We've written a main() function for you which asks the user for a number, calls your code for double(num) , and prints the result.

Here's a sample run of the program (user input in bold italics):

Enter a number: 2 Double that is 4
"""

# Solution 

def double_num(num):
  return num * 2

def get_input():
  while True:
    try:
      user_input = int(input("Enter a number: "))
      break
    except ValueError:
      print("Invalid input. Please enter an integer.")
  return user_input

def main():
  user_input = get_input()
  doubled_num = double_num(user_input)
  print(f"The doubled number of {user_input} is: {doubled_num}")

if __name__ == "__main__":
  main()