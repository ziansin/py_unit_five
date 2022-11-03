def multiplication_table(number):
    test = ""
    for x in range(number, number * 13, number):
        test += str(x) + " "
    return(test)
    """
    Ex. multiplication_table(6) returns "6 12 18 24 30 36 42 48 54 60 66 72 "
    :param number: An integer
    :return: A string of 12 values representing the mulitiplication table of the parameter number.
    """

def main():
        print(multiplication_table(6))

if __name__ == '__main__':
        main()
