# The Konditorei coffee shop sells coffee at $10.50 a pound plus the cost of shipping.
# Each order ships for $0.86 per pound + $1.50 fixed cost for overhead.
# Write a function that calculates the cost of an order.
#
#
# Assume the user needs to input the number of pounds of the order.
# Make sure the output acts like a bill of sale showing the appropriate values.

def order():
    print("This function calculates the cost of an order.")
    pound = eval(input("Enter how many pounds you plan to purchase: "))
    subtotal = 10.50 * pound
    shipping = (0.86 * pound) + 1.50
    total = subtotal + shipping
    print("Subtotal: $",subtotal)
    print("Shipping: $",shipping)
    print("Total:    $",total)
