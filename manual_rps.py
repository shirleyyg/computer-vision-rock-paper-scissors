import random

def get_computer_choice():
    options = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(options)
    return computer_choice

def get_user_choice():
    user_choice = input("Pick an option between Rock, Paper and Scissors....").strip().capitalize()
    while user_choice not in ["Rock", "Paper", "Scissors"]:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
        user_choice = input("Pick an option between Rock, Paper and Scissors....").strip().capitalize()
    return user_choice

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        return "It's a tie"
    elif computer_choice == 'Rock' and user_choice == 'Scissors':
        return "You lost!"
    elif computer_choice == 'Scissors' and user_choice == 'Paper':
        return "You lost!"
    elif computer_choice == 'Paper' and user_choice == 'Rock':
        return "You lost!"
    else:
        return "You win!"
    
def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    result = get_winner(computer_choice, user_choice)
    
    print(f"Computer chose {computer_choice}.")
    print(f"You chose {user_choice}.")
    print(result)

play()