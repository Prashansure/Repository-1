# ISSUE 56
#
# Problem:
# Write a program that accepts a number and recursively extracts all digits that satisfy a given condition.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def even_digits(number):
    digits = str(abs(number))
    def collect(index):
        # TODO: Check the recursive stopping condition for the string of digits.
        if index >= len(digits):
            return []
        digit = int(digits[index])
        rest = collect(index + 1)
        # TODO: Check the condition used to select digits.
        if digit % 2 == 1:
            return [digit] + rest
        return rest
    # TODO: Check where the first digit is read.
    return collect(0)

def check_solution():
    assert even_digits(52847) == [2, 8, 4]
    assert even_digits(135) == []
    assert even_digits(0) == [0]

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
