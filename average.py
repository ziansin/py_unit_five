total = 0
num = 0

while True:
    user_in = input("Write a number: ")
    if user_in == "q":
        break
    user_in_int = int(user_in)
    total = user_in_int + total
    """
    num is used to find out how many numbers are put in by the user
    Each time the user inputs something, the num increases by 1
    """
    num += 1

average = total / num
print("The average is:", average)
