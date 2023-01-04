#Zain Pilcher
#12/1/22
#Program for guessing number game

import random
def get_number():
    """
    Gets a random number to be used for the game
    :return: The random number generated of type integer
    """
    number = random.randint(1,100)  #generates the random number between 1 and 100
    return number


def get_guess():
    """
    Gets the user input if it is between 1 and 100. If it does not fill the requirements, then the user is prompted to answer again.
    :return: The user's guess between 1 and 100 of type integer
    """
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))    # asks the user for their input
        except ValueError:
            print("Not an integer")                                     # if the user input is not an integer, it will prompt the user again
            continue
        else:
            if guess <= 100 and guess >= 1:                             # checks if the guess is between 1 and 100
                return guess
                break
def main():
    """
    Compares the user's answer to the computer generated answer
    If the answer is too high or too low, the function will say so
    """
    total = 0                           # the total number of guesses
    for x in range(3):                  # the game is played for a total of 3 times
        number = get_number()           # creates the new random number for the user to guess by calling the get_number function
        print("Game", (x + 1))          # displays the game number
        guess = get_guess()             # asks the user for their input by calling the get_guess function
        guesses = 0                     # declares the number of guesses as 0
        while True:
            if guess > number:          # tells the user if their guess is too high
                print("Too high")
                guesses += 1            # adds 1 to the total number of guesses
                guess = get_guess()     # asks the user for their input again
            elif guess < number:        # tells the user if their guess is too low
                print("Too low")
                guesses += 1            # adds 1 to the total number of guesses
                guess = get_guess()     # asks the user for their input again
            elif guess == number:       # if the user's guess is equal to the generated number, they win
                print("You win")
                guesses += 1
                print("The number was", number)                                     # the generated number is shown
                print("Your total number of guesses for this game:", guesses)       # gives the user the number of guesses they needed to take
                print("")
                total = total + guesses # adds the number of guesses for each game to the total number of guesses
                break
    average = (total / 3)               # finds the average number of guesses for 3 games by dividing the total by 3
    print("The average number of guesses is:", average)
    if average <= 8:                    # the user is congratulated if they get a lower average (if it is less than or equal to 9)
        print("Great job!!!!!!")
    elif average > 8:                   # the user is told to do better next time if their average is higher than 9
        print("Try to get a smaller average next time")
    print("Thanks for playing")

main()

