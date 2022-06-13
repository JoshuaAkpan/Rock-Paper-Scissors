# from json import load
import random


game_options = ["R" , "P" , "S"]

#initialize game
def init():

    is_input_valid = False
    intro = "rock-paper-scissors v1.0 \xa9Akpan".upper()
    about = "ABOUT=> Rock-Paper-Scissors is a simple two-player game where, at a signal, \nplayers make figures with their hands, representing a rock, a piece of paper, or a pair of scissors.\n"
    hint = "HINTS: There are 3 sides; R, P, S \n Choose carefully \n'R' represents Rock & Rock beats Scissors \n'P' represents Paper & Paper beats Rock \n'S' represents Scissors & Scissors beats Paper"

    print("--------------------------------")
    print (intro)
    print("--------------------------------")
    print(about)
    print("--------------------------------")
    print(hint)
    print("--------------------------------")
    print ("Welcome Player!")
    print()

    while is_input_valid == False:

        # ACCEPTING PLAYER INPUT
        player_choice = (input("Choose a side: R, P or S : \n")).upper()

        print(f"You played :-> {player_choice}")
        print("")


        if(player_choice in game_options):
            is_input_valid = True


        # COMPUTER RESULT
            computer_choice = (random.choice(game_options))

            if computer_choice == "R":
                computer_choice = "Rock"
            elif computer_choice == "P":
                computer_choice = "Paper"
            else:
                computer_choice = "Scissors"

        # PLAYER RESULT

            if player_choice == "R":
                player_choice = "Rock"
            elif player_choice == "P":
                player_choice = "Paper"
            else:
                player_choice = "Scissors"

            print(users(player_choice, computer_choice))

        # GAME LOGIC
            tie(player_choice,computer_choice)
            win(player_choice,computer_choice)
            
            

        else:
            print("  ___      ___     ___    ____  ")
            print(" /   \    /   \   ||  \  ( (  \ ")
            print("(     )  (     )  ||__/   \ \    ")
            print(" \___/    \___/   ||     __) )  ")
            print("Error!!: Input is not amongst selection. Try again.")
            print("--------------------------------")




def users(player,computer):
    result = (f"Player ({player}) : CPU ({computer})")
    return result


def tie(player,computer):
    if {player} == {computer}:
        print("It is a tie, TRY AGAIN")
        init()
        



def win(player,computer):
    # IF PLAYER WINS
    if f"{player}" in "Rock" and f"{computer}" in "Scissors":
        print("YOU WIN!!: As Rock crushes Scissors")

    elif f"{player}" == "Scissors" and f"{computer}" == "Paper":
        print("YOU WIN!!: As Scissors shreds Paper")

    elif f"{player}" == "Paper" and f"{computer}" == "Rock":
        print("YOU WIN!!: As Paper blinds Rock")

    # IF COMPUTER WINS
    elif f"{player}" == "Scissors" and f"{computer}" == "Rock":
        print("COMPUTER WINS!!: As Rock crushes Scissors")

    elif f"{player}" == "Paper" and f"{computer}" == "Scissors":
        print("COMPUTER WINS!!: As Scissors shreds Paper")

    elif f"{player}" == "Rock" and f"{computer}" == "Paper":
        print("COMPUTER WINS!!: As Paper blinds Rock")


    



#GAMEEEEEEE ON
init()

