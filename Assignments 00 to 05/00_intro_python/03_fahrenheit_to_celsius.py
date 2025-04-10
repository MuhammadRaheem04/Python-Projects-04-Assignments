
# Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius. 

# The equation you should use for converting from Fahrenheit to Celsius is the following:
# degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

# Here's a sample run of the program (user input is in bold italics):

# Enter temperature in Fahrenheit: 76
# Temperature: 76.0F = 24.444444444444443C

# Solution 

def main():
    try:
        degrees_fahrenheit : float = float(input("Enter temperature in Fahrenheit: "))
        degrees_celsius : int = (degrees_fahrenheit - 32) * 5.0/9.0 

        print(f"Temprature: {degrees_fahrenheit:.1f}F = {degrees_celsius}C")

    except ValueError:
        print("Invalid input! Please enter a numeric value.")

if __name__ == '__main__':
    main()