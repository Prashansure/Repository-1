# ISSUE 9
#
# Problem:
# Write a program that accepts a list of words and checks which words are palindromes using a function.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def palindromes(words):
    result = []
    for word in words:
        # TODO: Check how a word is compared with its reverse.
        if word != word[::-1]:
            result.append(word)
    # TODO: Check whether mixed-case words should be considered palindromes.
    return result
    # TODO: Check whether the result preserves the required information.
    # TODO: Check behavior when the input contains only one item.
    # TODO: Check the result when there are no matching values.
    # TODO: Check that the calculation uses the intended values.

def check_solution():
    assert palindromes(["level", "cat", "radar"]) == ["level", "radar"]
    assert palindromes(["noon"]) == ["noon"]
    assert palindromes(["Level", "python"]) == ["Level"]

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
