# ISSUE 29
#
# Problem:
# Write a program that accepts a list of integers and recursively creates a new list containing only the values that satisfy a given condition.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def keep_even(values):
    def visit(index):
        # TODO: Check the recursive stopping condition.
        if index == len(values):
            return []
        rest = visit(index + 1)
        value = values[index]
        # TODO: Check the condition for retaining a value.
        if value % 2 == 1:
            # TODO: Check how the current item is placed in the result.
            # TODO: Check where the current value belongs in the filtered sequence.
            return rest + [value]
        return rest
    # TODO: Check which index begins the recursive filter.
    return visit(0)

def check_solution():
    assert keep_even([3, 4, 6, 7]) == [4, 6]
    assert keep_even([]) == []

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
