# rock paper scissors game
import datetime
import random
from rps_functions import convert_human, convert_computer_input, who_wins

print("Rock, Paper Scissors Game - Let's play!\nThe rules are: Rock smashes Scissors, Paper wraps Rock and Scissors cut"
      " Paper!\n ***********************************************")

# list of possible actions
actions = ["Rock", "Paper", "Scissors"]

player_name = input("Enter your name: ")


while True:
    human_choice = input("Please select your fighter: R = Rock, P = Paper, S = Scissors: ")

# calling convert_human(human) and saving the output to the variable human_action
    human_action = convert_human(human_choice)

    # to cover invalid input scenario
    if human_action == "Invalid input":
        print("Please enter a valid input, R, P or S")
        continue

# printing what the player chose
    print("You chose: {}".format(human_action))

# generating random number for computer input
    computer_input = random.randint(0, 2)
    computer_action = convert_computer_input(computer_input)
    print("The computer chose: {}".format(computer_action))

# create variables for keeping score

    player_score = 0
    computer_score = 0

# compares user's choice against computer's choice and then display a message as to if the user won, lost or drew

    who_wins(human_action, computer_action)


# ask them if they want to play again, any input other than Y/y will break the loop and exit

    play_again = input("Do you want to play again? (Y/N): ")
    if play_again.upper() != "Y":
        current_time = datetime.datetime.now()
        dt_string = current_time.strftime("%d/%m/%Y %H:%M:%S")
        score_file = open("rps.txt", 'a')
        score_file.write(dt_string + "     " + str(player_name) + "     " + "human victories: " + str(player_score) +
                         "     " + "computer victories: " + str(computer_score))
        score_file.write("\n -------------------------------------------------------------------------------------- \n")
        score_file.close()
        break

