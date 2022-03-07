# function to convert human choice

def convert_human(human):
    actions = ["Rock", "Paper", "Scissors"]
    if human.upper() == "R":
        human_choice = actions[0]
    elif human.upper() == "P":
        human_choice = actions[1]
    elif human.upper() == "S":
        human_choice = actions[2]
    else:
        human_choice = "Invalid input"

    return human_choice

# function to convert computer input

def convert_computer_input(computer_input):
    actions = ["Rock", "Paper", "Scissors"]
    computer_input_choice = actions[computer_input]
    return computer_input_choice

# function to decide who wins

def who_wins(human_action, computer_action):
    player_score = 0
    computer_score = 0

    if human_action == computer_action:
        print("Both players selected the same, it is a tie")

    elif human_action == "Rock":
        if computer_action == "Scissors":
            print("Rock breaks scissors, so you are victorious!")
            player_score += 1
        else:
            print("Paper wraps rock, so you have been defeated")
            computer_score += 1
    elif human_action == "Paper":
        if computer_action == "Rock":
            print("Paper wraps rock, so you are victorious!")
            player_score += 1

        else:
            print("Scissors cut paper, so you have been defeated")
            computer_score += 1
    elif human_action == "Scissors":
        if computer_action == "Paper":
            print("Scissors cut paper, so you are victorious!")
            player_score += 1
        else:
            print("Rock breaks scissors, so you have been defeated")
            computer_score += 1

        print("Total human victories = ", player_score, "Total computer victories = ", computer_score)


