# ISSUE 14
#
# Problem:
# Write a program that accepts a list of temperatures in Celsius and converts every temperature to Fahrenheit using a function.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def to_fahrenheit(celsius_values):
    converted = []
    for celsius in celsius_values:
        # TODO: Check the conversion formula and its order of operations.
        converted.append(celsius * 9 / 5 - 32)
    # TODO: Check that a converted value is kept for each input.
    return converted
    # TODO: Check whether the result preserves the required information.
    # TODO: Check behavior when the input contains only one item.
    # TODO: Check the result when there are no matching values.
    # TODO: Check that the calculation uses the intended values.

def check_solution():
    assert to_fahrenheit([0, 100]) == [32, 212]
    assert to_fahrenheit([-40]) == [-40]
    assert to_fahrenheit([]) == []

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
