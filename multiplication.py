def multiplication_table(number):
    test = ""
    if number != 0:
        for x in range(number, number * 13, number):
            test += str(x) + " "
        return(test)
    elif number == 0:
        for x in range(12):
            test += str(0) + " "
        return(test)
    """
    Ex. multiplication_table(6) returns "6 12 18 24 30 36 42 48 54 60 66 72 "
    :param number: An integer
    :return: A string of 12 values representing the mulitiplication table of the parameter number.
    """

def main():
        print(multiplication_table(-5))

if __name__ == '__main__':
        main()
