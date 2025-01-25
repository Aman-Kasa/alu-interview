#!/usr/bin/python3
"""In a text file, there is a single character H. Your text editor can execute
only two operations in this file: Copy All and Paste. Given a number n, write
a method that calculates the fewest number of operations needed to result in
exactly n H characters in the file.
"""


def minOperations(n):
    if n <= 1:
        return 0
    
    operations = 0
    divisor = 2  # Start from the smallest possible divisor
    
    # Try to factor n with all possible divisors
    while divisor * divisor <= n:
        while n % divisor == 0:
            operations += divisor  # Add the divisor to the operations
            n //= divisor  # Reduce n by the divisor
        divisor += 1
    
    # If n is greater than 1, it means n itself is a prime factor
    if n > 1:
    operations += n
    return operations
   