
# Problem Statement 

# Write a program which prompts the user to type an affirmation of your choice (we'll use "I am capable of doing anything I put my mind to.") until they type it correctly.

# Here's a sample run of the program (user input is in blue):

# Please type the following affirmation: I am capable of doing anything I put my mind to. Hmmm That was not the affirmation. Please type the following affirmation: I am capable of doing anything I put my mind to. I am capable of doing anything I put my mind to. That's right! :)


# Solution :

AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation: " + AFFIRMATION + "\n")

    user_feedback = input()  # Get user's input
    while user_feedback != AFFIRMATION:  # While the user's input isn't the affirmation
        # Tell the user that they did not type the affirmation correctly
        print("Hmmm... That was not the affirmation. Let's try again.")

        # Ask the user to type the affirmation again!
        print("Please type the following affirmation: " + AFFIRMATION + "\n")
        user_feedback = input()

    print("That's right! :)")


if __name__ == '__main__':
    main()