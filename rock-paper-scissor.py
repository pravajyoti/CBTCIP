import random
while True: 
    user_input = input("Enter your choice(rock,paper,scissors)")
    possible_choices = ("rock", "paper", "scissors")
    computer_input = random.choice(possible_choices)

    print(f"You chose: {user_input}, computer chose: {computer_input}")

    if user_input == computer_input:
        print(f"its a draw, both selected: {user_input}")

    elif user_input == "rock":
        if computer_input == "scissors":
            print(f"user wins as rock will break the scissors")
        else:
            print(f"user lose as paper will cover rock")

    elif user_input == "paper":
        if computer_input == "rock":
            print(f"user wins as paper will cover rock")
        else:
            print(f"user lose as scissor will cut the paper")

    elif user_input == "scissors":
        if computer_input == "paper":
            print(f"user wins as scissor will cut paper")
        else:
            print(f"user lose as rock will break scissors") 

    play_again = input("Do you want to play again? (y/n):")
    if play_again.lower() != "y":
        break
print("Game over!")


