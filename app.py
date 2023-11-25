# Write mini-game logic for rock-paper-scissors game handle user inputs, putting them in lowercase and informing the user if the option is invalid.
# Write a function that randomly returns one of the 3 options.
# Write a function that checks who won.
# Write a function that starts the game and calls the other functions.

import random   # import random module

def game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Please choose one of the following: Rock, Paper, Scissors")
    user_choice = input("Enter your choice: ").lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("You win!")
        else:
            print("You lose!")
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("You win!")
        else:
            print("You lose!")
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("You win!")
        else:
            print("You lose!")
    else:
        print("Invalid input. Please try again.")
    play_again = input("Would you like to play again? (y/n): ").lower()
    if play_again == "y":
        game()
    else:
        print("Thanks for playing!")

game()

