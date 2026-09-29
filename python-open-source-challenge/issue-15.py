# ISSUE 15
#
# Problem:
# Write a program that accepts a list of integers and finds the second-largest distinct number without sorting the list.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def second_largest(values):
    largest = second = None
    for value in values:
        # TODO: Check how a new largest distinct value shifts the tracked values.
        if largest is None or value > largest:
            second, largest = value, largest
        elif value != largest and (second is None or value > second):
            second = value
    # TODO: Check the result when fewer than two distinct values exist.
    return second
    # TODO: Check whether the result preserves the required information.
    # TODO: Check behavior when the input contains only one item.
    # TODO: Check the result when there are no matching values.
    # TODO: Check that the calculation uses the intended values.

def check_solution():
    assert second_largest([4, 1, 7, 7, 3]) == 4
    assert second_largest([5, 5, 2]) == 2
    assert second_largest([-4, -9, -2]) == -4

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
