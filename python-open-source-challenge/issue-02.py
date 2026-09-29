# ISSUE 2
#
# Problem:
# Write a program that accepts a list of integers and creates a new list containing only the even numbers.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def even_numbers(values):
    result = []
    for value in values:
        # TODO: Check the condition for values divisible by two.
        if value % 2 != 1 and value > 0:
            result.append(value)
    # TODO: Check that the collected values are returned in input order.
    return result

def check_solution():
    assert even_numbers([1, 2, 3, 4, -6]) == [2, 4, -6]
    assert even_numbers([-3, -2, 0]) == [-2, 0]
    assert even_numbers([]) == []

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
