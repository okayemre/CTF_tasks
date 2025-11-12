# Task 1: Robust Data Parser with Enhanced Error Handling

# Requirements
# 1.Function Definition: Implement a function parse_numbers(data_string) that accepts a comma-separated string.
# 2.Basic Error Control: Use try, except, else, and finally for comprehensive error control.
# Standard Exceptions:
# Catch ValueError if a part of the string is not a valid number (e.g., "10,abc,30"). Log this error (a simple print statement is sufficient) and continue processing the valid numbers.
# Catch IndexError if there's an issue accessing elements (e.g., with an empty string after splitting).
# Define a custom exception class, e.g., InvalidInputDataError, which is raised if the entire input string is empty or contains no valid data after cleaning (e.g., only commas or spaces).


str_list = ["1", "2", "3"]
value_error_list = ["1", "abc", "3"]
index_error_list = ["1", "2"]


def parse_numbers(data_string):

    int_list = []
    try:
        for number in data_string:
            int_list.append(int(number))
        data_string[2] = 6  # for index error
    except ValueError:
        print("Value Error")
    except IndexError:
        print("Index Error")
    else:
        print("Program succesfully")
    finally:
        print("Program Finish")

    return int_list


print("--------------------------------")
print(parse_numbers(str_list))
print("--------------------------------")
print(parse_numbers(value_error_list))
print("--------------------------------")
print(parse_numbers(index_error_list))
print("--------------------------------")


# Simple File Processing: Interacting with Files (Simple 035 Task)
print("--------------------------------")

file = open("my_notes.txt", "w")
file.write("This is a test file\n")
file.write("\nHi What`s up!!!")
file.close()

file = open("my_notes.txt", "a")
file.write("\n Hi Again!!!")
file.close()

file = open("my_notes.txt", "r")
content = file.read()
print(content)
file.close()
print("--------------------------------")

file = open("my_notes.txt", "r")
lines = file.readlines()
for line in lines:
    print(line)
file.close()
print("--------------------------------")


with open("my_notes_with.txt", "w") as file:
    file.write("1. This a new file with `with`")

with open("my_notes_with.txt", "a") as file:
    file.write("\n1. Hi with :)")

with open("my_notes_with.txt", "r") as file:
    content_with = file.read()
    print(content_with)

print("--------------------------------")

with open("my_notes_with.txt", "r") as file:
    content_with = file.readlines()
    for content in content_with:
        print(content)

print("--------------------------------")

with open("my_notes_with.txt", "w") as file:
    file.write("\n2. Hi with :)")

with open("my_notes_with.txt", "r") as file:
    content_with = file.readlines()
    for content in content_with:
        print(content)

print("--------------------------------")

with open("my_notes_with.txt", "w") as file:
    file.write("1. This a new file with `with`")
    file.write("\n2. Hi with :)")

with open("my_notes_with.txt", "r") as file:
    content_with = file.readlines()
    for content in content_with:
        print(content)

print("--------------------------------")
