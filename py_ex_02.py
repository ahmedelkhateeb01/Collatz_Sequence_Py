# Collatz Sequence using python.

# Creating a prompt for the user to add the number.
# First iteration.


def myNumber(userNumber):
    if userNumber <= 0:
        raise ValueError("input must be a positive integer.")
    while userNumber != 1:
        # userNumber = int(input("Enter the number: "))a
        if userNumber % 2 == 1:
            print(userNumber)
            userNumber = 3 * userNumber + 1
        elif userNumber % 2 == 0:
            print(userNumber)
            userNumber = userNumber // 2


# invoke the Function myNumber.
myNumber(20)
print("\n******************************\n")
# invoke another function.
myNumber(21)
print("\n****************************************************************\n")  # noqa: E501
print("This the first \'Commit_01\'")

print("\n****************************************************************\n")  # noqa: E501
