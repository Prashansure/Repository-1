# ISSUE 13
#
# Problem:
# Write a program that accepts a number n and generates all prime numbers from 1 to n using a function.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def primes_up_to(n):
    primes = []
    for candidate in range(2, n + 1):
        # TODO: Check what a divisor tells us about whether the candidate is prime.
        if all(candidate % divisor == 0 for divisor in range(2, int(candidate ** 0.5) + 1)):
            primes.append(candidate)
    # TODO: Check boundary values below the first prime.
    return primes
    # TODO: Check whether the result preserves the required information.
    # TODO: Check behavior when the input contains only one item.
    # TODO: Check the result when there are no matching values.
    # TODO: Check that the calculation uses the intended values.

def check_solution():
    assert primes_up_to(10) == [2, 3, 5, 7]
    assert primes_up_to(1) == []
    assert primes_up_to(2) == [2]

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
