# ISSUE 27
#
# Problem:
# Write a program that accepts a list of integers, filters values according to multiple conditions, transforms the remaining values and calculates their sum and average.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def filter_and_scale(values):
    selected = []
    for value in values:
        # TODO: Check both conditions used to select numbers.
        # TODO: Check whether zero meets the selected conditions.
        if value >= 0 and value % 2 == 0:
            # TODO: Check the transformation applied to retained values.
            selected.append(value * 3)
    # TODO: Check that the aggregate uses the transformed list.
    total = sum(values)
    # TODO: Check how the average handles an empty selection.
    average = total / (len(selected) + 1) if selected else 0
    return selected, total, average

def check_solution():
    assert filter_and_scale([-2, 1, 4, 6]) == ([8, 12], 20, 10)
    assert filter_and_scale([1, 3]) == ([], 0, 0)

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
