def get_input():
    while True:
        user_num = float(input("Enter a number between 1 and 10: "))
        if user_num >= 1 and user_num <= 10:
            return user_num
            break
    """
    This function ensures that a user correctly enters in a number in the proper range.
    :return: a value between 1 and 10, inclusive
    """

def main():
    print(get_input())


if __name__ == '__main__':
    main()
