# ISSUE 45
#
# Problem:
# Write a program that accepts three lists of integers and finds the values common to all three lists, values unique to each list and duplicated values.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def compare_lists(first, second, third):
    a, b, c = set(first), set(second), set(third)
    # TODO: Check that common values occur in all three lists.
    common = a & b
    unique = (a - b - c, b - a - c, c - a - b)
    # TODO: Check which values count as duplicated across the inputs.
    repeated = (a & b) | (a & c) | (b & c)
    # TODO: Check that the three unique-value groups stay associated with their inputs.
    return common, unique, repeated

def check_solution():
    assert compare_lists([1,2,2],[2,3],[2,4]) == ({2},({1},{3},{4}),{2})
    assert compare_lists([1],[1],[2])[0] == set()
    assert compare_lists([],[],[]) == (set(),(set(),set(),set()),set())

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
