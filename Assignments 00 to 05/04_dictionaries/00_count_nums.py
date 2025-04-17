
# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this:

# Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number: 6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 4 appears 2 times. 6 appears 1 times. 12 appears 1 times.

# Solution:

def get_user_numbers():
   
    user_numbers = []
    while True:
        user_input = input("Enter a number or type done to finish: ")
        
        # If the user enters a blank line, break out of the loop and stop asking for input
        if user_input.lower() == "done":
            break
        
        # convert the user input to an integer and add it to the list
        try:
            num = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        user_numbers.append(num)
    
    return user_numbers

def count_nums(num_lst):
   
    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    
    return num_dict


def print_counts(num_dict):
  
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times.")
        

def main():

    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)
    print(num_dict)


if __name__ == '__main__':
    main()