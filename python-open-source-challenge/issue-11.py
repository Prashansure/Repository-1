# ISSUE 11
#
# Problem:
# Write a program that accepts a list of integers and counts how many are positive, negative and zero.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def count_signs(values):
    counts = {"positive": 0, "negative": 0, "zero": 0}
    for value in values:
        # TODO: Check that zero is counted separately from positive values.
        if value >= 0: counts["positive"] += 1
        elif value < 0: counts["negative"] += 1
        else: counts["zero"] += 1
    # TODO: Check the complete set of counts.
    return counts
    # TODO: Check whether the result preserves the required information.
    # TODO: Check behavior when the input contains only one item.
    # TODO: Check the result when there are no matching values.
    # TODO: Check that the calculation uses the intended values.

def check_solution():
    assert count_signs([-2, 0, 3, 0]) == {"positive": 1, "negative": 1, "zero": 2}
    assert count_signs([]) == {"positive": 0, "negative": 0, "zero": 0}
    assert count_signs([-1, 1, 0]) == {"positive": 1, "negative": 1, "zero": 1}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
