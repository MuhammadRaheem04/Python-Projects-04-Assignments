
# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

# What's your favorite animal? cow

# My favorite animal is also cow!

# Solution: 

def main():
    while True:
        try:
            # Ask the user for their favorite animal
            animal : str = input("What's your favorite animal? ")


            # Validate: Check if input contains only letters and spaces
            if not animal.replace(" ", "").isalpha():
                raise ValueError("Please enter a valid animal name (letters only).")

            # If valid, print the response and break the loop
            print("My favorite animal is also " + animal + "!")
            break  
        

        except ValueError as e:
            print(e)  # Show error message and ask again
if __name__ == '__main__':
        main()

    
