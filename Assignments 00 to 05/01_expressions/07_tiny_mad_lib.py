
# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

# Here's a sample run:

# Please type an adjective and press enter. tiny

# Please type a noun and press enter. plant

# Please type a verb and press enter. fly

# Code in Place is fun. I learned to program and used Python to make my tiny plant fly!

# Solution:

SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my " # adjective noun verb

def main():
    # Get the three inputs from the user to make the adlib
    while True:
        try:
            # Get the adjective from user input
            adjective: str = input("Please type an adjective and press enter. ")
            if not adjective.replace(" ", "").isalpha():
                print("Please enter a valid adjective (Letters only).")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid adjective.")
            continue
        break
    while True:
        try:
            # Get the noun from user input
            noun: str = input("Please type a noun and press enter. ")
            if not noun.replace(" ", "").isalpha():
                print("Please enter a valid noun (Letters only).")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid noun.")
            continue
        break
    while True:
        try:
            # Get the verb from user input
            verb: str = input("Please type a verb and press enter. ")
            if not verb.replace(" ", "").isalpha():
                print("Please enter a valid verb (Letters only).")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid verb.")
            continue
        break

    # Join the inputs together with the sentence starter
    print(SENTENCE_START + adjective + " " + noun + " " + verb + "!")


if __name__ == '__main__':
    main()