import random

print("===== ROCK PAPER SCISSORS GAME =====")

user_score = 0
computer_score = 0

while True:
    print("\nChoose an option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    user_input = input("Enter your choice (1/2/3): ")

    if user_input == "1":
        user_choice = "rock"

    elif user_input == "2":
        user_choice = "paper"

    elif user_input == "3":
        user_choice = "scissors"

    else:
        print("Invalid option! Please select 1, 2 or 3.")
        continue

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print("\nYour choice:", user_choice)
    print("Computer choice:", computer_choice)

    if user_choice == computer_choice:
        print("Result: It's a tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or
        (user_choice == "scissors" and computer_choice == "paper")
        or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("Result: You win!")
        user_score += 1

    else:
        print("Result: Computer wins!")
        computer_score += 1

    print("\n----- SCORE -----")
    print("Your score:", user_score)
    print("Computer score:", computer_score)

    again = input("\nDo you want to play again? (yes/no): ").lower()

    if again != "yes":
        print("\n===== FINAL SCORE =====")
        print("Your score:", user_score)
        print("Computer score:", computer_score)

        if user_score > computer_score:
            print("Congratulations! You won the game.")

        elif computer_score > user_score:
            print("Computer won the game.")

        else:
            print("The game ended in a tie.")

        print("Thank you for playing!")
        break
