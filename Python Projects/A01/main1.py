import random                   # the random library   


######################################################################
# This function receive the player and the computer numbers
# then use the if elif statement to determine who is the Pick_Winner
# or if we have a tie.
######################################################################

def Pick_Winner(player_Number, computer_Number):
                                # Check who won and print
    if computer_Number == 1 and player_Number == 2:
        return "Player wins!"
    
    elif computer_Number == 2 and player_Number == 1:
        return "Computer wins!"
    
    elif computer_Number == 3 and player_Number == 1:
        return "Player wins!"
    
    elif computer_Number == 1 and player_Number == 3:
        return "Computer wins!"
    
    elif computer_Number == 2 and player_Number == 3:
        return "Player wins!"
    
    elif computer_Number == 3 and player_Number == 2:
        return "Computer wins!"
    
    else:
        return "It is a Tie!, the game must be played again to determine the winner.!!!"


######################################################################
# This function assign the numbers 1 , 2 , 3 to the right description
# either a rock, paper or scissors.
######################################################################

def convert_Number(choice):
                                # Return respective value to number
    if choice == 1:
        return 'rock'
    elif choice == 2:
        return 'paper'
    else:
        return 'scissors'


######################################################################
# This function return the our random number generator from 1 to 3.
######################################################################

def getComputer_Number():
    return random.randint(1, 3)


######################################################################
# This function prompt the user and run as long as the player does 
# not enter the number 4 to terminate the program.
######################################################################

def getPlayer_Number():
                                # Ask user to enter either of four
    choice = int(input('1. rock, 2. paper, 3. scissors or 4 to exit: '))
                                # Keep asking till user enters a valid input
    while choice not in [1, 2, 3, 4]:
        choice = int(input('1 .rock, 2. paper, 3. scissors or 4 to exit: '))

    return choice


# Main
def main():
    player = getPlayer_Number()  # get the player choice
    comp = getComputer_Number()  # generate the computer choice
    while player != 4:          # while the user has not chosen 4
                                # print the player choice as a string
        print('Player''s Choice:', convert_Number(player))
                                # print the computer choice as a string
        print('Computer''s Choice:', convert_Number(comp))
                                # print the winner as a string
        print(Pick_Winner(player, comp))

        print()
                                # get new choices for the player and computer
        player = getPlayer_Number()
        comp = getComputer_Number()


if __name__ == '__main__':
    main()