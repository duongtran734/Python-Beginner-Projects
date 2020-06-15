from random import *

"""
TicTacToe App (command line based)
"""

# global variable board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# display board
def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}\t\t1 , 2 , 3")
    print(f"{board[3]} | {board[4]} | {board[5]}\t\t4 , 5 , 6")
    print(f"{board[6]} | {board[7]} | {board[8]}\t\t7 , 8 , 9")


# check for win conditions
def check_win_conditions():
    if horizontal() or vertical() or diagonal():
        return True


# check for horizontal wins
def horizontal():
    if (board[0] == 'x' and board[1] == 'x' and board[2] == 'x') \
            or (board[3] == 'x' and board[4] == 'x' and board[5] == 'x') \
            or (board[6] == 'x' and board[7] == 'x' and board[8] == 'x'):
        return 'winner x'
    elif (board[0] == 'o' and board[1] == 'o' and board[2] == 'o') \
            or (board[3] == 'o' and board[4] == 'o' and board[5] == 'o') \
            or (board[6] == 'o' and board[7] == 'o' and board[8] == 'o'):
        return 'winner o'
    else:
        return False
    # check for vertical


# check for vertical wins
def vertical():
    if (board[0] == 'x' and board[3] == 'x' and board[6] == 'x') \
            or (board[1] == 'x' and board[4] == 'x' and board[7] == 'x') \
            or (board[2] == 'x' and board[5] == 'x' and board[8] == 'x'):
        return 'winner x'
    elif (board[0] == 'o' and board[3] == 'o' and board[6] == 'o') \
            or (board[1] == 'o' and board[4] == 'o' and board[7] == 'o') \
            or (board[2] == 'o' and board[5] == 'o' and board[8] == 'o'):
        return 'winner o'
    else:
        return False
    # check for diagonal


# check for diagonal wins
def diagonal():
    if (board[0] == 'x' and board[4] == 'x' and board[8] == 'x') \
            or (board[2] == 'x' and board[4] == 'x' and board[6] == 'x'):
        return 'winner x'
    elif (board[0] == 'o' and board[4] == 'o' and board[8] == 'o') \
            or (board[2] == 'o' and board[4] == 'o' and board[6] == 'o'):
        return 'winner o'
    else:
        return False


# check if board is full
def board_full():
    for i in board:
        if i == '-':
            return False
    return True


# check for tie
def check_tie():
    if (not check_win_conditions()) and board_full():
        return True


# reset board
def board_reset():
    global board
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]


# roll the dice to see who go first
def roll():
    dice1 = randrange(1, 7)
    dice2 = randrange(1, 7)
    total = dice1 + dice2
    return total


# check for who go first ( x or y)
'need modify'


def player_go_first():
    player1 = roll()
    player2 = roll()
    return 'x' if player1 > player2 else 'o'


# play game
def play_game():
    display_board()
    player_turn = player_go_first()
    print(f" {player_turn} go first. ")
    while True:
        placement(player_turn)
        if player_turn == 'x' and check_win_conditions():
            print('X win')
            break
        elif player_turn == 'o' and check_win_conditions():
            print('O win')
            break
        elif check_tie():
            print('Tie game, Play again')
            board_reset()
            display_board()
        player_turn = handle_turn(player_turn)
        print(f"{player_turn} turn.")


# pick a spot to spot on the board
def placement(player_turn):
    valid = False
    while not valid:
        choice = input("Pick a number from 1 - 9 corresponding to the board:\n")
        valid = validation(choice)
        if valid:
            board[int(choice) - 1] = player_turn
        else:
            print("Invalid input")
    display_board()


# check for valid input for placement
def validation(choice):
    try:
        val = int(choice)
        if val in (range(1, 10)) and board[val - 1] == '-':
            return True
    except Exception:
        return False


# handle turn
def handle_turn(go_first):
    return 'x' if go_first == 'o' else 'o'


def main():
    play_game()


if __name__ == "__main__":
    main()
