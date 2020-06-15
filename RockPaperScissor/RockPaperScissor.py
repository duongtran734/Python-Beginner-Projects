from random import *

'''
Make a rock-paper-scissors game where it is the player vs the computer.
The computer’s answer will be randomly generated,
 while the program will ask the user for their input.
 This project will better your understanding of while loops and if statements.
'''


# Get Computer Choice
def compChoice():
    lst = ['rock', 'paper', 'scissors']
    return choice(lst)


# Get Player Choice
def playerChoice():
    valid_choice = False
    while not valid_choice:
        choice = input("Enter in rock/paper/scissors as choice:\n").lower()
        if checkPlayerChoice(choice):
            return choice


# Validation for player choice
def checkPlayerChoice(choice):
    if choice == 'Rock' or choice == 'Paper' or choice == 'Scissors':
        return True
    else:
        print("Invalid input.")
        return False


# Run the game
def gamePlay():
    winner = False
    while not winner:
        cChoice = compChoice()
        pChoice = playerChoice()
        if (cChoice == 'rock' and pChoice == 'paper') or (cChoice == 'paper' and pChoice == 'scissors') or (
                cChoice == 'scissors' and pChoice == 'rock'):
            print("Player win")
            winner = True
        elif (cChoice == 'paper' and pChoice == 'rock') or (cChoice == 'scissors' and pChoice == 'paper') or (
                cChoice == 'rock' and pChoice == 'scissors'):
            print('Computer win')
            winner = True
        else:
            print('Draw')


def main():
    gamePlay()


if __name__ == '__main__':
    main()
