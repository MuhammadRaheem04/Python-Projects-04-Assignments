
import random

# List of Hangman stages (in reverse - full man to empty)
HANGMAN_PICS = [
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
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
       |   |
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
           |
           |
           |
           |
    ---------
    """
]

def hangman():
    print("🎯 Welcome to Reverse Hangman!")
    print("Each wrong guess removes a part of the man. Don’t let him disappear!\n")

    # Dictionary of categories
    word_categories = {
        "1": ("Fruits", ["banana", "mango", "apple", "guava", "peach"]),
        "2": ("Animals", ["elephant", "tiger", "goat", "cat", "donkey"]),
        "3": ("Desi Foods", ["biryani", "haleem", "nihari", "samosa", "pakora"])
    }

    # Show category options (but NO word selection)
    print("Choose a category:")
    for key, (cat_name, _) in word_categories.items():
        print(f"{key}. {cat_name}")

    while True:
        choice = input("Enter category number: ")
        if choice in word_categories:
            category_name, words_list = word_categories[choice]
            word = random.choice(words_list)  # Random word
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

    guessed_letters = []
    wrong_guesses = 0
    max_wrong = len(HANGMAN_PICS) - 1

    print(f"\n🔤 The word has {len(word)} letters.")
    print("_ " * len(word))

    # Game loop
    while True:
        # Show current man
        print(HANGMAN_PICS[wrong_guesses])

        # Input guess
        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("⛔ Enter only one letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that.")
            continue

        guessed_letters.append(guess)

        # Correct or not
        if guess in word:
            print("✅ Correct!")
        else:
            print("❌ Wrong!")
            wrong_guesses += 1

        # Show word progress
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word.strip())

        # Win check
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 You saved the man! YOU WIN! 🏆")
            break

        # Lose check
        if wrong_guesses >= max_wrong:
            print(HANGMAN_PICS[wrong_guesses])
            print(f"\n💀 The man is gone! You lost. The word was: '{word}'")
            break

# Run it!
if __name__ == "__main__":
    hangman()
