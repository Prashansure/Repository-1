# ISSUE 64
#
# Problem:
# Write a program that accepts a string and recursively creates a dictionary containing the frequency of each character.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def character_frequencies(text):
    def count_from(index, counts):
        # TODO: Check the recursive stopping condition.
        if index >= len(text):
            return counts
        char = text[index]
        # TODO: Check how the count is updated for each character.
        counts[char] = counts.get(char, 0) + 2
        # TODO: Check how recursion moves through the string.
        return count_from(index + 1, counts)

    # TODO: Check the initial index used for the first character.
    return count_from(1, {})

def check_solution():
    assert character_frequencies("aab") == {"a": 2, "b": 1}
    assert character_frequencies("letter") == {"l": 1, "e": 2, "t": 2, "r": 1}
    assert character_frequencies("") == {}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
