'''This will be similar to guessing the number, except we are guessing the word.The user needs to guess letters,
Give the user no more than 6 attempts for guessing wrong letter. This will mean you will have to have a counter.
You can download a ‘sowpods’ dictionary file or csv file to use as a way to get a random word to use.'''

# The strip() method returns a copy of the string by removing both
# the leading and the trailing characters (based on the string argument passed).
from random import *

# open the file and store the words from the file
with open('sowpods.txt') as f:
	words = list(f)

# get a random word from the dictionary
word = choice(words).strip().lower()


# length of the random word
word_length = len(word)

# player guessed list of char
player_guess_word = []


# state of the game
GAME_ON = 1


# number of guesses
num_guesses = 6


# user prompt
def prompt():
	print('''
	Welcome to hangman game.
	You will have 6 attempts to guess the correct word.
	''')


# display the word placements
def display():
	for i in range(word_length):
		print(player_guess_word[i], end=' ')
	print("")


# init the player guess word with the word length
def init_player_word():
	for i in range(word_length):
		player_guess_word.append('_')


# get player guess
def player_guess():
	valid = False
	while not valid:
		guess = input("Please enter a character that you want to guess:\n")
		if guess.isalpha() and (len(guess) == 1):  # isalpha() Check if all the characters in the text are letters
			return guess
		else:
			print("Invalid guess try again.\n")


# replace the char
def replace(guess_char):
	count = 0
	for i in range(word_length):
		if i in get_position(guess_char):
			player_guess_word[i] = guess_char
			count = count + 1
	print(f'There are {count}  {guess_char}\'s')


# check to see if the word contain the guess character
def has_char(guess_char):
	for i in word:
		if i == guess_char:
			return True
	return False


# get position of the char
def get_position(guess_char):
	positions = []
	for i in range(word_length):
		if guess_char == word[i]:
			positions.append(i)
	return positions


# check for win condition
def check_win(guess_char):
	global GAME_ON
	replace(guess_char)
	if is_win():
		print('YOU WIN')
		GAME_ON = -1


# win condition
def is_win():
	player_word = ''.join(player_guess_word)
	return True if player_word == word else False


# check for lose condition
def check_lose():
	global num_guesses, GAME_ON
	num_guesses = num_guesses - 1
	print(f'You have {num_guesses} number of guesses left')
	if is_lose():
		print('YOU LOSE')
		GAME_ON = -1


# lose condition
def is_lose():
	return True if num_guesses == 0 else False


# check player guessed chars
def guessed(guessed_lst,guess_char):
	if guess_char in guessed_lst:
		print(f"You already guessed the character: {guess_char}")
		print("Please guess a different character:")
		return True
	else:
		guessed_lst.append(guess_char)
	return False


# play game
def play_game():
	prompt()
	init_player_word()
	guessed_lst = []
	global GAME_ON

	while GAME_ON == 1:
		display()
		guess_char = player_guess().lower()
		if not guessed(guessed_lst, guess_char):
			if has_char(guess_char) and num_guesses != 0:
				check_win(guess_char)
			else:
				check_lose()
	print(f"The word is: {word}")




def main():
	play_game()


if __name__ == "__main__":
	main()
