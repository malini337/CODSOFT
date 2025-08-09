import random

# Available choices
choices = ['rock', 'paper', 'scissors']

# Initialize scores
user_score = 0
computer_score = 0

print("🎮 Welcome to Rock, Paper, Scissors Game!")
print("Instructions: Type 'rock', 'paper', or 'scissors' to play. Type 'exit' to quit.\n")

# Game loop
while True:
    # User input
    user_choice = input("Your choice (rock/paper/scissors): ").lower()

    if user_choice == 'exit':
        print("Thanks for playing!")
        break
    if user_choice not in choices:
        print("Invalid input. Please choose rock, paper, or scissors.\n")
        continue

    # Computer choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Game logic
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        result = "You win! 🎉"
        user_score += 1
    else:
        result = "Computer wins! 💻"
        computer_score += 1

    # Display result
    print(f"Result: {result}")
    print(f"Score => You: {user_score} | Computer: {computer_score}\n")

    # Ask if user wants to play again
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("👋 Exiting the game. Final Scores:")
        print(f"🏁 You: {user_score} | 💻 Computer: {computer_score}")
        break
