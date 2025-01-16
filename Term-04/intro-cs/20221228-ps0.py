"""
Write a program that does the following in order:
1. Asks the user to enter a number “x”
2. Asks the user to enter a number “y” 
3. Prints out number “x”, raised to the power “y”.
4. Prints out the log (base 2) of “x”. 
"""

old_message = """
Enter number x: 2
Enter number y: 3
X**y = 8
log(x) = 1
"""

import math

x = int(input("Enter number x: "))
y = int(input("Enter number y: "))
print("X**y = " + str(x**y))
print("log(x) = " + str(int(math.log(x,2))))

new_message = """
Enter number x: 2
Enter number y: 3
X**y = 8
log(x) = 1
"""

# This is just to double check that the values that I get from my code match the example exactly. 
#print(old_message == new_message)

