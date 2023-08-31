import random
#ٌRead the player to enter their choice
def get_player_choice():
    while True:
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice. Please try again.")
            
#Generate a random choice for the computer
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

#Determine the winner Who is win By Compare the player's choice with the computer's choice 
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"
    
#Display a welcome message and the game rules to the players.
def display_WelcomeAndRoles_massage():
    print("Welcome to Rock Paper Scissors Game!")
    print("Let's play a game of Rock Paper Scissors against the computer.\n\t Done By:Ghamdan Al-Yamani")
    print("--------\t Game Rules : ----- \n Rock : kill --> scissors. \n scissors : kill --> paper. \n paper : kill --> rock.")
    print()   
        
# the main function --- > play_game()
def play_game():
    player_score = 0
    computer_score = 0
    tries = 6

    display_WelcomeAndRoles_massage()

    while tries > 0:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)
        print(result)

        if result == "You win!":
            player_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        tries -= 1
        print(f"\nTries left: {tries}")
        print(f"Player score: {player_score}")
        print(f"Computer score: {computer_score}")

        if player_score == 3:
            print("\n*------\t Congratulations! You won! ------*")
            break
        elif computer_score == 3:
            print("\n*------\t Sorry, the computer won! -----*")
            break
#Display the final scores of the player and the computer and a farewell message to wrap up the game.
    print("\n-----\t Final scores: -------- ")
    print(f"\t\tPlayer score: {player_score}")
    print(f"\t\tComputer score: {computer_score}")
    print("\nThank you for playing. Have a good day!\n\t SALLAM *-*")

# Start the game --- > Call main function
play_game()