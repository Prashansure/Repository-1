# ISSUE 76
#
# Problem:
# Write a program that accepts a list of integers and finds all unique pairs whose sum is equal to a given target value.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def pairs_for_target(numbers, target):
    pairs = set()
    for index, first in enumerate(numbers):
        # TODO: Check that a number is paired only with a later position.
        for second in numbers[index:]:
            if first + second == target:
                # TODO: Check how duplicate pairs are represented.
                pairs.add((first, second))
    # TODO: Check that pair order does not create duplicate results.
    return pairs

def check_solution():
    assert pairs_for_target([1,2,3,4,2],5) == {(1,4),(2,3)}
    assert pairs_for_target([1,1,1],2) == {(1,1)}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
