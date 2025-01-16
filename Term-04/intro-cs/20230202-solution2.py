# Palindrome checker: Write a program that checks if a given string is a palindrome, i.e., if it reads the same forwards and backwards.

# By Jonathan A. McCormick, Jr.

"""
user_string = input("Enter a string and I will check whether or not it is a palendrome: ")

def reverse_string(string):
    try:
        if len(string) == 0:
            raise ValueError("Error: Cannot reverse an empty string")
        else:
            return string[::-1]
    except ValueError as e:
        return e

def palindrome_check(string):
    try:
        reverse = reverse_string(string)
        if string == reverse:
            return string + " is a palendrome."
        else:
            return string + " is NOT a palendrome."
            
    except ValueError as e:
        return e

print(palindrome_check(user_string))
"""

# ChatGPT suggested improvements
# ChatGPT: This code is well organized, has good use of functions and error handling, but with some improvements to be made. Here are some suggestions:
# You can simplify reverse_string function by using a ternary operator instead of a try-except block.
# Consider using if not string instead of if len(string) == 0 for an empty string check.
# Consider using f-strings instead of concatenation to format the output string.
# Add a type check in palindrome_check to ensure string is a string, otherwise return an error message.
# Here's an updated version of your code:

user_string = input("Enter a string and I will check whether or not it is a palendrome: ")

def reverse_string(string):
    return string[::-1] if string else "Error: Cannot reverse an empty string"

def palindrome_check(string):
    if not isinstance(string, str):
        return "Error: Input must be a string"
    reverse = reverse_string(string)
    return f"{string} is a palindrome." if string == reverse else f"{string} is NOT a palindrome."

print(palindrome_check(user_string))
