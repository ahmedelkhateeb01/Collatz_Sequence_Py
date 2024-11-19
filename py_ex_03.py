# This code from Chat GPT.


# intentionally left blank.


def collatz(number):
    if number % 2 == 0:
        # Even number
        result = number // 2
    else:
        # Odd number
        result = 3 * number + 1

    print(result)
    return result


# Main program
try:
    user_input = int(input("Enter an integer: "))  # Ensure the input is converted to an integer  # noqa: E501

    while user_input != 1:  # Keep looping until the result is 1
        user_input = collatz(user_input)  # Call collatz() and update the value of user_input  # noqa: E501

except ValueError:
    print("Please enter a valid integer.")
