# 1. Interactive Number Assistant

# The program should prompt the user to enter an integer.
# number_int = input("\nEnter a integer number: ")
number_int = int(input("\nEnter a integer number: "))

# If the input is not a valid integer, an error message should be displayed, and the user should be prompted for input again. Give the user a maximum of 3 attempts. After 3 failed attempts, the program should terminate with a polite message.

attempt = 1  # An entry has already been made above.
max_attempts = 3

while type(number_int) is not int:
    print("Wrong Type")
    number_int = input("\nEnter a right integer number:")
    attempt += 1
    if type(number_int) is not int and attempt < max_attempts:
        continue
    elif type(number_int) is not int and attempt == max_attempts:
        print("3 entry rights have expired")
        break
    else:
        break

# !!! The program isn't working properly. Because if we take the input as int, the system will throw an error without allowing an incorrect value to be entered. This problem can be solved with 'try' 'except', but it is not necessary at this stage.

# *******************************************************

# The number must be in the range of 1 to 1000 (inclusive). If it is outside this range, an appropriate message should be displayed, and the user should also be prompted for input again, without consuming an attempt (this is a value error, not a format error).


while True:
    if number_int >= 1 and number_int <= 1000:
        break
    else:
        print("Wrong range, it muss (1 - 1000)")
        number_int = int(input("\nEnter a integer number:"))
        continue


# *******************************************************


# Is the number even or odd?

if number_int % 2 == 0:
    print(f"{number_int} is even")
else:
    print(f"{number_int} is odd")


# Is the number a multiple of 7 and/or 13?

if number_int % 7 == 0 and number_int % 13 == 0:
    print(f"{number_int} is multiple of 7 and 13")
elif number_int % 7 == 0 or number_int % 13 == 0:
    print(f"{number_int} is multiple of 7 or 13")
else:
    print(f"{number_int} is not multiple of 7 or 13")
