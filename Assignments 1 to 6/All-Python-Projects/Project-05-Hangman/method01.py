import random

def hangman():
    print("Welcome to Hangman Game")
    print("Guess the word, letter by letter!\n")

    # Step 1: Dictionary with categories
    word_categories = {
        "Fruits": ["banana", "mango", "apple", "guava", "peach"],
        "Animals": ["elephant", "tiger", "goat", "cat", "donkey"],
        "Desi Foods": ["biryani", "haleem", "nihari", "samosa", "pakora"]
    }

    # Step 2: Choose a random category and word
    category = random.choice(list(word_categories.keys()))
    word = random.choice(word_categories[category]).lower()

    guessed_letters = []
    wrong_guesses = 0
    max_attempts = 6

    print(f"Category: {category}")
    print("_ " * len(word))

    # Step 3: Game loop
    while True:
        guess = input("Guess a letter: ").lower()

        # Check input
        if len(guess) != 1 or not guess.isalpha():
            print("⛔ Please enter a single letter (a-z only).")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            wrong_guesses += 1
            print(f"❌ Wrong! Attempts left: {max_attempts - wrong_guesses}")
        else:
            print("✅ Good guess!")

        # Display current progress
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word.strip())

        # Check for win
        if all(letter in guessed_letters for letter in word):
            print("🎉 You guessed it! Mubarak ho, you WON! 🏆")
            break

        # Check for loss
        if wrong_guesses >= max_attempts:
            print(f"💀 Game over! The word was '{word}'. Try again next time.")
            break

# Run the game
if __name__ == "__main__":
    hangman()


