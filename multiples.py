def get_sum(number):
    sum = 0
    for x in range(0, number):
        if x % 3 == 0 or x % 5 == 0:
            sum = x + sum
    return(sum)
    """
    Will return the sum of all the multiples of 3 or 5 of the given number.
    Ex. get_sum(10) returns 23
    :param number: The value up to which we want to find the sum. Not included in the calculation
    :return: The sum of all the multiples of 3 or 5 up to the number.
    """

def main():
    print(get_sum(10))

main()



