# ISSUE 23
#
# Problem:
# Write a program that accepts a list of integers and rearranges them so that the
# rarest numbers come first. Numbers that occur the same number of times keep the
# order in which they first appeared in the input.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def frequency_order(values):
    counts = {}
    for value in values:
        # TODO: Check how each occurrence changes the count.
        counts[value] = counts.get(value, 0) + 1
    # TODO: Check the order used for numbers with different frequencies.
    return sorted(values, key=lambda value: (counts[value], value))

def check_solution():
    assert frequency_order([4, 4, 1, 2, 2, 2, 1]) == [4, 4, 1, 1, 2, 2, 2]
    assert frequency_order([3, 1, 3, 2]) == [1, 2, 3, 3]
    assert frequency_order([]) == []

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
