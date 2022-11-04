def fibonacci(x):
    test = ""
    a = 0
    b = 1
    for y in range(x - 2):
        c = a + b
        a = b
        b = c
        c = a + b
        test += str(c) + " "
    if x > 1:
        return "1 " + "1 " + str(test)
    else:
        return "1 "
    """
    Ex. fibonacci(5) returns "1 1 2 3 5 "
    :param number: The number of Fibonacci terms to return
    :return: A string consisting of a number of terms of the Fibonacci sequence.
    """
def main():
    print((fibonacci(5)))

main()

