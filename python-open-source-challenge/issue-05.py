# ISSUE 5
#
# Problem:
# Write a program that accepts a sentence and reverses every word without changing the order of the words.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def reverse_words(sentence):
    words = sentence.split()
    reversed_words = []
    for word in words:
        # TODO: Check how characters inside each word are ordered.
        reversed_words.append(word[::-1])
    # TODO: Check that the original word order remains unchanged.
    # TODO: Check whether the words themselves stay in their original order.
    return " ".join(reversed_words[::-1])
    # TODO: Check whether the result preserves the required information.
    # TODO: Check behavior when the input contains only one item.
    # TODO: Check the result when there are no matching values.
    # TODO: Check that the calculation uses the intended values.

def check_solution():
    assert reverse_words("hello world") == "olleh dlrow"
    assert reverse_words("a bc") == "a cb"
    assert reverse_words("") == ""

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
