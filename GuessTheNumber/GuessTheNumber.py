from random import *


# Write a programme where the computer randomly generates a number between 0 and 20.
# The user needs to guess what the number is. If the user guesses wrong,
# tell them their guess is either too high, or too low.
# This will get you started with the random library if you haven't already used it.


# Get input from user
def getInput():
    result = input("Guess a number from 0 - 20 inclusive:\n")
    return result


# Check if to see if the input is an integer
def checkInput(input):
    try:
        val = int(input)
        return True
    except Exception:
        print("Invalid input try again")
        return False


# Check to see if the user guess it correct
def checkGuessNumb(user_input, randNumb):
    if user_input > randNumb:
        print("Your Guess is too high. Try again")
        return False
    elif user_input < randNumb:
        print("Your Guess is too low. Try again")
        return False
    else:
        print("You Win")
        return True


def main():
    randNumber = randint(0, 20)  # generate a random number from 0 - 20
    print(randNumber)
    gameOver = False
    while not gameOver:
        user_input = getInput()
        if checkInput(user_input):
            gameOver = checkGuessNumb(int(user_input), randNumber)


if __name__ == '__main__':
    main()
