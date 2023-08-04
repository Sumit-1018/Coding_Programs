import random
user_score=0
cpu_score=0

while True:
    user_action = input("Enter a choice (Rock, Paper, Scissors): ")
    user_action = user_action.capitalize()
    possible_actions = ["Rock", "Paper", "Scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!") 

    elif user_action == "Rock":
        if computer_action == "Scissors":
            print("Rock smashes Scissors! You win!")
            user_score+=1

        else:
            print("Paper covers Rock! You lose.")
            cpu_score+=1

    elif user_action == "Paper":
        if computer_action == "Rock":
            print("Paper covers Rock! You win!")
            user_score+=1

        else:
            print("Scissors cuts Paper! You lose.")
            cpu_score+=1

    elif user_action == "Scissors":
        if computer_action == "Paper":
            print("Scissors cuts Paper! You win!")
            user_score+=1

        else:
            print("Rock smashes Scissors! You lose.")
            cpu_score+=1
    
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        print(f'''\nFinal Score:
                CPU:{cpu_score}
                User:{user_score}\n''')
        break