
# Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

# 4.0 squared is 16.0

# solution: 

def main():
  while True:
    try:
      user_input: float = float(input("Enter a number to see it's Square: "))
      break
    except ValueError:
      print("Invalid input. Please enter a number.")
  square: float = user_input ** 2
  print(f"The square of {user_input} is {square}.")

if __name__ == "__main__":
  main()
