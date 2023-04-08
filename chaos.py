# This is a chaotic function, in which the values that have been displayed appear
# to be chaotic and without structure.

def chaos():
    print("This function represents a chaotic function.")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range (10):
        x = 3.9 * x * (1 - x)
        print(x)

# Exercise 3, page 24

def newchaos():
    print("This is a modified version of a chaotic function, where instead of 3.9, we multiply by 2.0")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range (10):
        x = 2.0 * x * (1 - x)
        print(x)

# Exercise 4, page 25

def chaos_output_20():
    print("This version of the chaotic function outputs 20 values, instead of 10.")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range (20):
        x = 3.9 * x * (1 - x)
        print(x)

# Exercise 5, page 25

def customchaos():
    print("This version of the chaotic function outputs a custom amount of values, instead of 10.")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print?"))
    for i in range (n):
        x = 3.9 * x * (1 - x)
        print(x)

# The following 3 functions use versions of the chaos function that are mathematically
# equivalent to each other
# Exercise 6a, page 25

def chaos_a():
    print("This function represents a chaotic function.")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range (100):
        x = 3.9 * x * (1 - x)
        print(x)

# Exercise 6b, page 25

def chaos_b():
    print("This function represents a chaotic function.")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range (100):
        x = 3.9 * (x - x * x)
        print(x)

# Exercise 6c, page 25

def chaos_c():
    print("This function represents a chaotic function.")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range (100):
        x = 3.9 * x - 3.9 * x * x
        print(x)
