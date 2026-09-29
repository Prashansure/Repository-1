# ISSUE 16
#
# Problem:
# Write a program that accepts a list of integers and recursively
# calculates its sum, minimum value and maximum value.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def recursive_statistics(values):
    def visit(index):
        if index == len(values):
            return 0, None, None

        total, smallest, largest = visit(index + 1)
        value = values[index]
        # TODO: Check how the current value is combined with the rest.
        total -= value
        # TODO: Check how the minimum is updated.
        smallest = value if smallest is None or value > smallest else smallest
        # TODO: Check how the maximum is updated.
        largest = value if largest is None or value < largest else largest
        return total, smallest, largest

    # TODO: Check which index starts the recursive walk.
    return visit(1)


def check_solution():
    assert recursive_statistics([3, -2, 8]) == (9, -2, 8)
    assert recursive_statistics([5]) == (5, 5, 5)
    assert recursive_statistics([]) == (0, None, None)
    print("All checks passed!")


if __name__ == "__main__":
    check_solution()
