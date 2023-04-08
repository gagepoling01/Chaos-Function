# This is a chaotic function, in which the values that have been displayed appear
# to be chaotic and without structure.

def chaos():
    print("This function represents a chaotic function.")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range (10):
        x = 3.9 * x * (1 - x)
        print(x)

# Exercise 1
# Modify the chaos program using 2.0 in place of 3.9 as the multiplier in the logistic function. 
# Your modified line of code should look like this:
#
# x = 2.0 * x * (1 - x)
# 
# Run the program for varius input values and compare the results of those obtained from the original program.

def newchaos():
    print("This is a modified version of a chaotic function, where instead of 3.9, we multiply by 2.0")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range (10):
        x = 2.0 * x * (1 - x)
        print(x)

# Exercise 2
# Modify the chaos program so that it prints out 20 values instead of 10.

def chaos_output_20():
    print("This version of the chaotic function outputs 20 values, instead of 10.")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range (20):
        x = 3.9 * x * (1 - x)
        print(x)

# Exercise 3
# Modify the chaos program so that the number of values to print is determined by the user.
# You will have to add a line near the top of the program to get another value from the user:
#
# n = eval(input("How many numbers should I print? "))
#
# Then you will need to change the loop to use n instead of a specific number.

def customchaos():
    print("This version of the chaotic function outputs a custom amount of values, instead of 10.")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print?"))
    for i in range (n):
        x = 3.9 * x * (1 - x)
        print(x)

# Exercise 4
# The calculation performed in the chaos program can be written in a number of ways
# that are algebraically equivalent. Write a version of the program for each of the
# following ways of doing the computation. Have your modified program print out 100
# iterations of the calculation and compare the results when run on the same input.
#
# a) 3.9 * x * (1 - x)
# b) 3.9 * (x - x * x)
# c) 3.9 * x - 3.9 * x * x

# Exercise 4a
def chaos_a():
    print("This function represents a chaotic function.")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range (100):
        x = 3.9 * x * (1 - x)
        print(x)

# Exercise 4b
def chaos_b():
    print("This function represents a chaotic function.")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range (100):
        x = 3.9 * (x - x * x)
        print(x)

# Exercise 4c
def chaos_c():
    print("This function represents a chaotic function.")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range (100):
        x = 3.9 * x - 3.9 * x * x
        print(x)
