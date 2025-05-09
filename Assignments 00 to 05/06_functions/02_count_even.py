
# Problem Statement

# Fill out the function count_even(lst) which first populates a list by prompting the user for integers until they press enter (please use the prompt "Enter an integer or press enter to stop: "),

# and then prints the number of even numbers in the list.

# If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!

# Solution 


def count_even(lst):

    count = 0  # Stores the count of even numbers in the list
    for num in lst:  # Loop through the numbers in the list
        if num % 2 == 0:  # If the current number in the list is even (divisible by 2)
            count += 1  # Add one to our count!

    print(f"There are {count} even numbers in your selected list.")  # Print out how many even numbers we counted above

def get_list_of_ints():
    """
    Reads in integers until the user presses enter and returns the resulting list.
    """
    lst = []  # Make an empty list to store integers

    while True:
        user_input = input("Enter an integer or press enter to stop: ")  # Get user input for an integer
        
        if user_input == '':
            break  # If the user pressed enter, break out of the loop
        try:
            number = int(user_input)  # Try to cast the user input into an integer
            lst.append(number)  # Append the integer to the list
        except ValueError:  # If the user input is not an integer, print an error message and continue to the next iteration
            print("Please enter a valid integer.")

    return lst

def main():
    lst = get_list_of_ints()
    count_even(lst)

if __name__ == '__main__':
    main()