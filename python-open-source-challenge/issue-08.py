# ISSUE 8
#
# Problem:
# Write a program that accepts a list of integers and creates a new list containing only the odd numbers using a function.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def odd_numbers(values):
    result = []
    for value in values:
        # TODO: Check the condition for values with a remainder.
        if value % 2 == 0:
            result.append(value)
    # TODO: Check that negative odd values are kept in their original order.
    return result
    # TODO: Check whether the result preserves the required information.
    # TODO: Check behavior when the input contains only one item.
    # TODO: Check the result when there are no matching values.
    # TODO: Check that the calculation uses the intended values.

def check_solution():
    assert odd_numbers([1, 2, -3, 4]) == [1, -3]
    assert odd_numbers([-5, 0, 7]) == [-5, 7]
    assert odd_numbers([]) == []

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
