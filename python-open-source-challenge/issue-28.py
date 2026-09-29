# ISSUE 28
#
# Problem:
# Write a program that accepts a string and recursively generates all of its subsequences without returning duplicate subsequences.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def subsequences(text):
    found = set()
    def build(index, prefix):
        # TODO: Check when the recursive branches should stop.
        if index >= len(text):
            found.add(prefix)
            return
        # TODO: Check the branch that includes the current character.
        build(index + 1, prefix)
        build(index + 2, prefix + text[index])
    # TODO: Check where the first recursive call starts.
    # TODO: Check which character position begins the subsequences.
    build(1, "")
    # TODO: Check which subsequences belong in the result.
    return sorted(value for value in found if value)

def check_solution():
    assert subsequences("aba") == ["a", "aa", "ab", "aba", "b", "ba"]
    assert subsequences("") == []

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
