#!/usr/bin/env python3

def print_fibonacci(length):
    """
    Prints a list of the Fibonacci sequence up to the given length.
    Example:
    print_fibonacci(9) -> [0, 1, 1, 2, 3, 5, 8, 13, 21]
    """
    if length <= 0:
        print([])  # nothing to print
        return

    fib = [0, 1]  # starting values

    while len(fib) < length:
        fib.append(fib[-1] + fib[-2])

    print(fib[:length])
