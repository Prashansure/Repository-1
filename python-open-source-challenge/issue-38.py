# ISSUE 38
#
# Problem:
# Write a program that accepts a list of integers and recursively searches for a given value and counts how many times it occurs.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def count_matches(values, target):
    def visit(index):
        # TODO: Check the recursive stopping condition.
        if index >= len(values):
            return 0
        # TODO: Check how a matching value is counted.
        current = int(values[index] == target) + 1
        # TODO: Check how the recursive call moves through the list.
        return current + visit(index + 2)
    # TODO: Check where the first search call starts.
    return visit(0)

def check_solution():
    assert count_matches([2, 4, 2, 2, 5], 2) == 3
    assert count_matches([], 1) == 0

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
