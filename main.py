import logging

logging.basicConfig(level=logging.ERROR, filename="calculator.log", filemode="w")

import math

try:
    var1 = int(input("Enter first value for division: "))
    var2 = int(input("Enter second value for division: "))

    result = var1 / var2

    print(result)

except:
    logging.error("An error occurred in the code!")

try:
    var1 = int(input("Enter first value for multiplication: "))
    var2 = int(input("Enter second value for multiplication: "))

    result = var1 * var2

    print(result)

except:
    logging.error("An error occurred in the code!")

try:
    var1 = int(input("Enter first value for subtraction: "))
    var2 = int(input("Enter second value for subtraction: "))

    result = var1 - var2

    print(result)

except:
    logging.error("An error occurred in the code!")

try:
    var1 = int(input("Enter first value for sum: "))
    var2 = int(input("Enter second value for sum: "))

    result = var1 + var2

    print(result)

except:
    logging.error("An error occurred in the code!")

try:
    var1 = int(input("Enter first value for exponentiation: "))

    result = print(math.sqrt(var1))

except:
    logging.error("An error occurred in the code!")

try:
    var1 = int(input("Enter first value for square root: "))

    result = print(math.pow(var1))

except:
    logging.error("An error occurred in the code!")