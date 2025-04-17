import random

# Hangman parts - built as the player makes mistakes
HANGMAN_PICS = [
    """
       -----
       |   |
           |
           |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    ---------
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    ---------
    """
]

def hangman():
    print("🎉 Welcome to Hangman!")
    print("Guess the word letter by letter. Each wrong guess builds the man!\n")

    # Dictionary of categories and word lists
    word_categories = {
        "1": ("Fruits", ["banana", "mango", "apple", "guava", "peach"]),
        "2": ("Animals", ["elephant", "tiger", "goat", "cat", "donkey"]),
        "3": ("Desi Foods", ["biryani", "haleem", "nihari", "samosa", "pakora"])
    }

    # Display category choices
    print("Choose a category:")
    for key, (cat_name, _) in word_categories.items():
        print(f"{key}. {cat_name}")

    # Get valid category choice
    while True:
        choice = input("Enter category number: ")
        if choice in word_categories:
            category_name, words_list = word_categories[choice]
            word = random.choice(words_list)  # ✅ Word is randomly picked
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    guessed_letters = []
    wrong_guesses = 0
    max_attempts = len(HANGMAN_PICS) - 1

    print(f"\nYou selected category: {category_name}")
    print("_ " * len(word))

    # Game loop
    while True:
        print(HANGMAN_PICS[wrong_guesses])
        guess = input("Guess a letter: ").lower()

        # Input checks
        if len(guess) != 1 or not guess.isalpha():
            print("⛔ Please enter a single letter (a-z).")
            continue

        if guess in guessed_letters:
            print("⚠️ Already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            wrong_guesses += 1
            print(f"❌ Nope! Wrong guess. Tries left: {max_attempts - wrong_guesses}")
        else:
            print("✅ Nice! Correct letter.")

        # Show word progress
        display_word = ""
        for letter in word:
            display_word += letter + " " if letter in guessed_letters else "_ " # also can be wriiten as 

            # if letter in guessed_letters:
            #     display_word += letter + " "
            # else:
            #     display_word += "_ "

        print(display_word.strip())

        # Win check
        if all(letter in guessed_letters for letter in word):
            print("\n🏆 You guessed it! You win! 🎉")
            break

        # Lose check
        if wrong_guesses >= max_attempts:
            print(HANGMAN_PICS[wrong_guesses])
            print(f"\n💀 Game over! The word was '{word}'. Better luck next time.")
            break

# Run the game
if __name__ == "__main__":
    hangman()

