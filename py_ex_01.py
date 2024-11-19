# Continue practicing on function in python.
# import
# import
# import
# import


print("\n***********************************\n")  # This called a short separator.  # noqa: E501


print("\n*************************************************************************************\n")  # long separator# noqa: E501


# User input an value of variable called number
# number = int(input("Enter the value of the number: "))


# A Function called collatz
def collatz(number: int) -> int:
    while number != 1:
        try:
            if number % 2 == 0:
                return number // 2
            elif number % 2 == 1:
                return (number * 3) + 1
        # First exception.
        except ValueError:
            return "Error!, Please check out that all variables are the same type."  # noqa: E501
        # Second exception.
        except TypeError:
            return "Error!, One variable or more aren't integer."
        number = int(input("Enter the value of the number: "))


# Invoking the function collatz
collatz(1)
collatz(2)


print("\n*************************************************************************************\n")  # long separator# noqa: E501
# A


# A


# A


# A


# A


# A


# A


# A


print("\n***********************************\n")


print("\n*************************************************************************************\n")  # noqa: E501
