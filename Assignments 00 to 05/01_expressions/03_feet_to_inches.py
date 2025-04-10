
# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

# Solution:


INCHES_IN_FOOT: int = 12  # There are 12 inches for 1 foot.

def main():
    feet: float = float(input("Enter number of feet: "))  # Get the number of feet, make sure to cast it to a float!
    inches: float = feet * INCHES_IN_FOOT  # Perform the conversion
    print(f"{feet} feet is equal to {inches} inches!")
    
if __name__ == '__main__':
    main()