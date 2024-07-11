#!/usr/bin/python3
"""
Calculate minimum operations
to get exactly n 'H's
using Copy All and Paste
operations only.
"""


def minOperations(n):
    """
    Calculate minimum operations
    to get exactly n 'H's.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    return operations
