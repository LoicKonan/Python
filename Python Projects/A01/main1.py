import random

random.seed(300)

def determineWinner(playerChoice, computerChoice):
                                # Check who won and print
    if computerChoice == 1 and playerChoice == 2:
        return "Player wins!"
    
    elif computerChoice == 2 and playerChoice == 1:
        return "Computer wins!"
    
    elif computerChoice == 3 and playerChoice == 1:
        return "Player wins!"
    
    elif computerChoice == 1 and playerChoice == 3:
        return "Computer wins!"
    
    elif computerChoice == 2 and playerChoice == 3:
        return "Player wins!"
    
    elif computerChoice == 3 and playerChoice == 2:
        return "Computer wins!"
    
    else:
        return "It is a Tie!, the game must be played again to determine the winner.!!!"

def convertChoice(choice):
                                # Return respective value to number
    if choice == 1:
        return 'rock'
    elif choice == 2:
        return 'paper'
    else:
        return 'scissors'

def getComputerChoice():
    return random.randint(1, 3)

def getPlayerChoice():
                                # Ask user to enter either of four
    choice = int(input('1. rock, 2. paper, 3. scissors or 4 to exit: '))
                                # Keep asking till user enters a valid input
    while choice not in [1, 2, 3, 4]:
        choice = int(input('1 .rock, 2. paper, 3. scissors or 4 to exit: '))

    return choice


# Main
def main():
    player = getPlayerChoice()  # get the player choice
    comp = getComputerChoice()  # generate the computer choice
    while player != 4:          # while the user has not chosen 4
                                # print the player choice as a string
        print('Player''s Choice:', convertChoice(player))
                                # print the computer choice as a string
        print('Computer''s Choice:', convertChoice(comp))
                                # print the winner as a string
        print(determineWinner(player, comp))

        print()
                                # get new choices for the player and computer
        player = getPlayerChoice()
        comp = getComputerChoice()


if __name__ == '__main__':
    main()