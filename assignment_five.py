#Zain Pilcher
#11/9/22
#Program for guessing number game

import random
def get_number():
    number = random.randint(1,100)
    return number

def get_guess():
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess <= 100 and guess >= 1:
            return guess
            break
def main():
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

