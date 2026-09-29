# ISSUE 19
#
# Problem:
# Write a program that accepts a list of numbers and recursively transforms every element using a given mathematical operation.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def transform_values(values, operation):
    def visit(index):
        # TODO: Check when the recursive walk should stop.
        if index >= len(values):
            return []
        value = values[index]
        if operation == "double":
            changed = value * 2
        elif operation == "square":
            changed = value ** 2
        else:
            changed = value
        # TODO: Check how the current result is combined with later values.
        return [changed] + visit(index + 2)
    # TODO: Check where recursion begins.
    return visit(0)

def check_solution():
    assert transform_values([1, 2, 3], "square") == [1, 4, 9]
    assert transform_values([2, 4], "double") == [4, 8]
    assert transform_values([], "double") == []

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
