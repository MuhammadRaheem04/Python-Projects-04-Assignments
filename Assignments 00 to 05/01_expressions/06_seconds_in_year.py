
# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this:

# There are 5 seconds in a year!

# Solution:

# Useful constants to help make the math easier and cleaner!
DAYS_IN_YEAR: int = 365
HOURS_IN_DAY: int = 24
MIN_IN_HOUR: int = 60
SEC_IN_MIN: int = 60

def main():
   
   total_seconds: int = DAYS_IN_YEAR * HOURS_IN_DAY * MIN_IN_HOUR * SEC_IN_MIN  # Calculate the seconds 
   print(f"There are {total_seconds} seconds in a year!")

if __name__ == '__main__':
    main()