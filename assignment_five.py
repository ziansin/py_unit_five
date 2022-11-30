#Zain Pilcher
#11/30/22
#Program for guessing number game

import random
def get_number():
    '''
    :return: The random number generated
    '''
    number = random.randint(1,100)
    return number
    """
    Gets a random number to be used for the game
    """

def get_guess():
    '''
    :return: The user's guess between 1 and 100
    '''
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess <= 100 and guess >= 1:
            return guess
            break
    """
    Gets the user input if it is between 1 and 100. If it does not fill the requirements, then the user is prompted to answer again. 
    """
def main():
    """
    Compares the user's answer to the computer generated answer
    If the answer is too high or too low, the function will say so
    The user has three tries to guess the number otherwise they lose
    """
    number = get_number()
    guess = get_guess()
    if guess > number:
        print("Too high")
        guess_two = get_guess()
        if guess_two > number:
            print("Too high")
            guess_three = get_guess()
            if guess_three > number:
                print("You lose")
                print("The number was", number)
            elif guess_three < number:
                print("You lose")
                print("The number was", number)
            elif guess_three == number:
                print("You win")
                print("The number was", number)
        elif guess_two < number:
            print("Too low")
            guess_three = get_guess()
            if guess_three > number:
                print("You lose")
                print("The number was", number)
            elif guess_three < number:
                print("You lose")
                print("The number was", number)
            elif guess_three == number:
                print("You win")
                print("The number was", number)
        elif guess_two == number:
            print("You win")
            print("The number was", number)
    elif guess < number:
        print("Too low")
        guess_two = get_guess()
        if guess_two > number:
            print("Too high")
            guess_three = get_guess()
            if guess_three > number:
                print("You lose")
                print("The number was", number)
            elif guess_three < number:
                print("You lose")
                print("The number was", number)
            elif guess_three == number:
                print("You win")
                print("The number was", number)
        elif guess_two < number:
            print("Too low")
            guess_three = get_guess()
            if guess_three > number:
                print("You lose")
                print("The number was", number)
            elif guess_three < number:
                print("You lose")
                print("The number was", number)
            elif guess_three == number:
                print("You win")
                print("The number was", number)
        elif guess_two == number:
            print("You win")
            print("The number was", number)
    elif guess == number:
        print("You win")
        print("The number was", number)

main()

