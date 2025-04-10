
def mad_libs():
    print("Welcome to Mad Libs!")
    print("Please provide the following words to create a fun story.")

    noun: str = input("Give me a name: ")
    place: str = input("Give me a place: ")
    fun_adjective: str = input("Give me a fun adjective: ")
    random_object: str = input("Give me a random object: ")
    animal: str = input("Give me an animal: ")
    verb: str = input("Give me a verb: ")
    funny_exclamation: str = input("Give me a funny exclamation: ")

    # Create the story using the provided words
    story: str = f"""
    Once upon a time, in a land called {place}, there lived a {fun_adjective} {noun}.
    Every day, {noun} would {verb} with a {animal} and play with a {random_object}.
    One day, they discovered a magical {random_object} that could talk and grant wishes.
    {noun} and the {animal} were so excited that they shouted, "{funny_exclamation}!"
    They wished for a never-ending supply of {random_object} and lived happily ever after.
    """
    print("\nHere's your story:")
    print(story)
    print("Thanks for playing Mad Libs!")

if __name__ == "__main__":
    mad_libs()
