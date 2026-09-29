# ISSUE 71
#
# Problem:
# Write a program that accepts a list of words and recursively counts how many words have a length greater than a given value.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def count_long_words(words, minimum_length):
    def visit(index):
        # TODO: Check where the recursive walk should stop.
        if index >= len(words):
            return 0
        # TODO: Check how the current word is compared with the limit.
        current = int(len(words[index]) >= minimum_length)
        # TODO: Check that recursion visits each word.
        return current + visit(index + 2)
    return visit(0)

def check_solution():
    assert count_long_words(["pear","fig","plum","kiwi"], 3) == 3
    assert count_long_words([], 2) == 0

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
