
# Write a program that doubles each element in a list of numbers. For example, if you start with this list:

# numbers = [1, 2, 3, 4]

# You should end with this list:

# numbers = [2, 4, 6, 8]

# Solution:

def main():
    numbers: list[int] = [1, 2, 3, 4]  # Creates a list of numbers

    for i in range(len(numbers)):  # Loop through the indices of the list using range(len(numbers))
        elem_at_index = numbers[i]   # Get the element at index i in the numbers list
        numbers[i] = elem_at_index * 2  # Multiply the element by 2 and update the list at index i to double it

    print(numbers)  # This should print the doubled list

if __name__ == '__main__':
    main()