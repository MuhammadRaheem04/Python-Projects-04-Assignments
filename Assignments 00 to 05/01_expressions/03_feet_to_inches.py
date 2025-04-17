
# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

# Solution:


def main():
  inches_per_foot = 12
  while True:
    try:
      feet = float(input("Enter the length in feet: "))
      inches = feet * inches_per_foot
      print(f"{feet} feet is equal to {inches} inches.")
      break 
    except ValueError: 
      print("Invalid input. Please enter a number.")
if __name__ == '__main__':
  main()