import random

print("Welcome to the Rock, Paper, Scissor game!")

choices = ["rock", "paper", "scissor"]

user_score = computer_score = 0

print("Let's play!")
while True:
    user_input = input("Enter rock, paper, scissor or q to quit: ").lower()
    if user_input == "q":
        print(f"Your score: {user_score}")
        print(f"Computer score: {computer_score}")
        print("Thanks for playing!")
        break
    if user_input not in choices:
        print("Invalid choice! Try again.")
        continue
    computer_input = random.choice(choices)
    print(f"Computer chose: {computer_input}")
    if user_input == computer_input:
        print("It's a tie!")
    elif (user_input == "rock" and computer_input == "scissor") or \
         (user_input == "paper" and computer_input == "rock") or \
         (user_input == "scissor" and computer_input == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1
    print(f"Your score: {user_score}")
    print(f"Computer score: {computer_score}")
