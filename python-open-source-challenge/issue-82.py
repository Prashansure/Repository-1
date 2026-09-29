# ISSUE 82
#
# Problem:
# Write a program that accepts a list of integers and finds every repeated number along with its first and last position.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def repeated_positions(values):
    positions = {}
    for index, value in enumerate(values):
        # TODO: Check how the first occurrence position is retained.
        positions[value] = [index, index]
        # TODO: Check how later positions update the same value.
        positions[value][1] = index
    # TODO: Check that values occurring only once are excluded.
    return {value: tuple(bounds) for value, bounds in positions.items() if bounds[0] != bounds[1]}

def check_solution():
    assert repeated_positions([4,2,4,4,2]) == {4:(0,3),2:(1,4)}
    assert repeated_positions([1,2]) == {}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
