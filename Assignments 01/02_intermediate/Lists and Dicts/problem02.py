"""
Problem #2: Index Game
As a warmup, read this code and play the game a few times. Use this mental model of the list:

Objective:
Create a Python program that helps you practice accessing and manipulating elements in a list. This exercise will help you get comfortable with indexing, slicing, and modifying list elements.

Instructions:
Initialize a List:
Create a list with at least 5 different elements. They can be numbers, strings, or a mix of both.

Accessing Elements:
Write a function that:

Accepts a list and an index as inputs.
Returns the element at the specified index.
If the index is out of range, return an appropriate message.

Modifying Elements:
Write a function that:

Accepts a list, an index, and a new value as inputs.
Replaces the element at the specified index with the new value.
If the index is out of range, return an appropriate message.

Slicing the List:
Write a function that:

Accepts a list, a start index, and an end index as inputs.
Returns a new list containing the elements from the start index up to (but not including) the end index.
Handles cases where the indices are out of range.

Game Interaction:
Create a simple text-based game that:

Prompts the user to select an operation (access, modify, slice).
Asks for the necessary inputs (index, new value, etc.).
Displays the result and the updated list.
"""

# Solution: 

# Function to access an element at a given index
def access_element(my_list, index):
    try:
        return f"Element at index {index}: {my_list[index]}"
    except IndexError:
        return "Index out of range!"  # Handles cases where index is invalid

# Function to modify an element at a given index
def modify_element(my_list, index, new_value):
    try:
        old_value = my_list[index]  # Store old value to show change
        my_list[index] = new_value  # Replace with new value
        return f"Replaced '{old_value}' with '{new_value}'"
    except IndexError:
        return "Index out of range!"  # Error if index is invalid

# Function to return a slice from start to end index
def slice_list(my_list, start, end):
    try:
        return my_list[start:end]  # Return sublist
    except Exception:
        return "Invalid slicing indices!"  # Generic error message

# Main game function
def main():
    # Initialize the list with mixed data types
    my_list = ['apple', 42, 'banana', 3.14, 'grape']

    print("Welcome to the Index Game!")
    print(f"Your starting list: {my_list}")

    # Keep showing the menu until user chooses to exit
    while True:
        print("\nChoose an operation:")
        print("1. Access element")
        print("2. Modify element")
        print("3. Slice list")
        print("4. Show current list")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        # Option 1: Access element
        if choice == '1':
            index = int(input("Enter the index to access: "))
            print(access_element(my_list, index))

        # Option 2: Modify an element
        elif choice == '2':
            index = int(input("Enter the index to modify: "))
            new_value = input("Enter the new value: ")
            
            # Try converting to int or float if possible
            if new_value.isdigit():
                new_value = int(new_value)
            else:
                try:
                    new_value = float(new_value)
                except ValueError:
                    pass  # Keep it as string if not numeric

            print(modify_element(my_list, index, new_value))

        # Option 3: Slice the list
        elif choice == '3':
            start = int(input("Enter the start index: "))
            end = int(input("Enter the end index: "))
            result = slice_list(my_list, start, end)
            print(f"Sliced list: {result}")

        # Option 4: Show current list
        elif choice == '4':
            print(f"Current list: {my_list}")

        # Option 5: Exit the game
        elif choice == '5':
            print("Thanks for playing the Index Game! 👋")
            break

        # Invalid choice handling
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the game
if __name__ == "__main__":
    main()
