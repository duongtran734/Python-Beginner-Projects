'''
Create a random list of numbers between 0 and 100 with a difference of 2 between each number.
Ask the user for a number between 0 and 100 to check whether their number is in the list. The programme should work like this.
The programme will half the list of numbers and see whether the users number matches the middle element in the list.
If they do not match, the programme will check which half the number lies in, and eliminate the other half.
The search then continues on the remaining half, again checking whether the middle element in that half is equal to the user’s number.
This process keeps on going until the programme finds the users number, or until the size of the subarray is 0, which means the users number isn't in the list.
'''

from random import *


# create a random list of number 0-100, with difference of 2 between each number
def create_lst():
    lst = []
    for i in range(randrange(0, 51), randrange(51, 101), 2):
        lst.append(i)
    return lst


# get user input
def user_number():
    valid = False
    while not valid:
        try:
            numb = int(input("Please enter a whole number between 0 and 100:\n"))
            return numb
        except Exception:
            print("Invalid input try again.")


# binary search
def binary_search(lst, value):
    left = 0
    right = len(lst) - 1
    if left > right:
        return False
    while left <= right:
        mid = (left + right) // 2
        if value == lst[mid]:
            return True
        elif value > lst[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return False


def main():
    rand_lst = create_lst()
    user_input = user_number()
    if binary_search(rand_lst, user_input):
        print(f"Found number {user_input} in the list:\n{rand_lst}")
    else:
        print(f'The number {user_input} is not in the list:\n{rand_lst}')


if __name__ == "__main__":
    main()
