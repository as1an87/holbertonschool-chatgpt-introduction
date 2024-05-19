#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculates the factorial of a non-negative integer using recursion.

    Parameters:
    - n: An integer representing the number whose factorial is to be calculated.

    Returns:
    An integer representing the factorial of the input number 'n'.
    """

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get the command-line argument and calculate the factorial
f = factorial(int(sys.argv[1]))
print(f)

