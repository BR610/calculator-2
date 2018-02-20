"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
def user_proceed():
    """takes user input and determines whether to quit or tokenize input"""
    user_input = raw_input("Enter a command or 'q' to quit: ")
    n1 = user_input.split(" ")
    n = []
    print n1
    
    for i in n1[1:]:
        n.append(int(i))



    if user_input == "q":
        return
    #else:
        #tokenized_string = user_input.split(" ")
    #return tokenized_string

#def calculator(n):
    #""" Performs arithmetic calculations based on user preference"""

    elif n1[0] == '+':
        return add((n[0]), (n[1]))
    elif n1[0] == '-':
        return subtract(n[0], n[1])
    elif n1[0] == "*":
        return multiply(n[0], n[1])
    elif n1[0] == '/':
        return divide(n[0], n[1])
    elif n1[0] == 'square':
        return square(n[0])
    elif n1[0] == 'cube':
        return cube(n[0])
    elif n1[0] == 'pow':
        return power(n[0], n[1])
    elif n1[0] == 'mod':
        return mod(n[0], n[1])






