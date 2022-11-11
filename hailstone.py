def sequence(number):
    steps = 0
    if number == 2:
        steps = 1
        return steps
    elif number == 1:
        return steps
    else:
        while True:
            if number % 2 != 0 and number != 1:
                number = 3 * number + 1
                steps += 1
            elif number == 1:
                return steps
                break
            if number % 2 == 0:
                number = number / 2
                steps += 1

    """
    If the number n is odd - 3*n + 1
    If the number n is even n / 2
    :param number: The starting number for the Hailstone sequence
    :return: The number of steps taken to reach 1
    """

def main():
    num = int(input("Enter a number: "))
    if num == 2:
        print("There was 1 step")
    else:
        print("There were", sequence(num), "steps")

main()