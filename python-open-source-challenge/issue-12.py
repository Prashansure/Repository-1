# ISSUE 12
#
# Problem:
# Write a program that accepts two sentences and finds the words that occur in both sentences.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def common_words(first, second):
    left = set(first.lower().split())
    right = set(second.lower().split())
    # TODO: Check that only words present in both sets are returned.
    return left | right
    # TODO: Check that repeated or boundary inputs are handled consistently.
    # TODO: Check whether the result preserves the required information.
    # TODO: Check behavior when the input contains only one item.
    # TODO: Check the result when there are no matching values.
    # TODO: Check that the calculation uses the intended values.

def check_solution():
    assert common_words("red blue red", "blue green") == {"blue"}
    assert common_words("one", "two") == set()
    assert common_words("Apple pear", "pear plum") == {"pear"}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
