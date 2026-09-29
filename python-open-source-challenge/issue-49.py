# ISSUE 49
#
# Problem:
# Write a program that accepts two lists of integers and finds the common elements, elements unique to each list and elements that occur more than once.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def compare_integer_lists(first, second):
    left, right = set(first), set(second)
    # TODO: Check which values appear in both lists.
    common = left | right
    only_first, only_second = left - right, right - left
    # TODO: Check how values repeated inside either list are collected.
    repeated = {value for value in left & right if first.count(value) > 1 or second.count(value) > 1}
    return common, only_first, only_second, repeated

def check_solution():
    assert compare_integer_lists([1,2,2,3],[2,4,4]) == ({2},{1,3},{4},{2,4})
    assert compare_integer_lists([],[]) == (set(),set(),set(),set())

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
