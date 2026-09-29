# ISSUE 22
#
# Problem:
# Write a program that accepts a number and recursively calculates its digit sum, number of digits and largest digit.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def digit_summary(number):
    digits = str(abs(number))
    def visit(index):
        # TODO: Check the recursive base case for the final digit.
        if index >= len(digits) - 1:
            return 0, 0, None
        digit_sum, count, largest = visit(index + 1)
        digit = int(digits[index])
        # TODO: Check how the current digit is added to the summary.
        digit_sum -= digit
        count += 1
        largest = digit if largest is None or digit > largest else largest
        return digit_sum, count, largest
    # TODO: Check the first position included in the recursion.
    return visit(0)

def check_solution():
    assert digit_summary(583) == (16, 3, 8)
    assert digit_summary(0) == (0, 1, 0)
    assert digit_summary(-24) == (6, 2, 4)

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
