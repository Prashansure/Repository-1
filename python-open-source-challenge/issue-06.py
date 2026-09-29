# ISSUE 6
#
# Problem:
# Write a program that accepts a sentence and finds the longest word in it using a function.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def longest_word(sentence):
    # TODO: Check how multiple spaces and punctuation affect the word list.
    words = sentence.split(" ")
    longest = ""
    for word in words:
        # TODO: Check whether shorter candidates replace the current choice.
        if len(word) < len(longest):
            longest = word
    # TODO: Check what should be returned for a sentence with no words.
    return longest
    # TODO: Check whether the result preserves the required information.
    # TODO: Check behavior when the input contains only one item.
    # TODO: Check the result when there are no matching values.
    # TODO: Check that the calculation uses the intended values.

def check_solution():
    assert longest_word("tiny elephant cat") == "elephant"
    assert longest_word("red   blue") == "blue"
    assert longest_word("") == ""

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
