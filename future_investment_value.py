# Function A
#   A function to compute the value of an investment
#   carried 10 years into the future
#   It's set up to add your yearly investment before APR is calculated,
#   as logically you'll make more money that way.

def future_value_a():
    print("This program calculates the future value")
    print("of an investment, with a time of your choosing.")

    principal = eval(input("Enter the initial principal: "))
    investment = eval(input("Enter your yearly investment: "))
    apr = eval(input("Enter the annual interest rate as an integer: "))
    time = eval(input("Enter time passed in years: "))

    for i in range(time):
        principal = (principal + investment) * (1 + (apr/100))

    print("The value in",time,"years is:",principal)

# Function B
#   A function to compute the value of an investment
#   carried 10 years into the future with compounding periods of your choice

def future_value_b():
    print("This program calculates the future value")
    print("of an investment after 10 years, with compounding periods of your choice.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate as an integer: "))
    period = eval(input("How many compounding periods per year? "))
    time = eval(input("Enter the time passed in years: "))

    for i in range(time * period):
        principal = principal * (1 + ((apr/100)/period))

    print("The value after",time * period,"compounding periods will be:",principal)

# Function C
#   The same function as A, except it displays each individual
#   calculation for each year.

def future_value_c():
    print("This program calculates the future value")
    print("of an investment, with a time of your choosing.")

    principal = eval(input("Enter the initial principal: "))
    investment = eval(input("Enter your yearly investment: "))
    apr = eval(input("Enter the annual interest rate as an integer: "))
    time = eval(input("Enter time passed in years: "))

    for i in range(time):
        principal = (principal + investment) * (1 + (apr/100))
        print(principal)


# Function D
#   The same function as B, except it displays each individual
#   calculation for each year.

def future_value_d():
    print("This program calculates the future value")
    print("of an investment after 10 years, with compounding periods of your choice.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate as an integer: "))
    period = eval(input("How many compounding periods per year? "))
    time = eval(input("Enter the time passed in years: "))

    for i in range(time * period):
        principal = principal * (1 + ((apr/100)/period))
        print(principal)
