#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    Calculates the factorial of a non-negative integer n using recursion.
    The factorial of n is the product of all positive integers less than 
    or equal to n.

    Parameters:
    n (int): The non-negative integer to calculate the factorial of.

    Returns:
    int: The calculated factorial of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Execution block
if __name__ == "__main__":
    if len(sys.argv) > 1:
        f = factorial(int(sys.argv[1]))
        print(f)
