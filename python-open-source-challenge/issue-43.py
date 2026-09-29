# ISSUE 43
#
# Problem:
# Write a program that accepts a paragraph and finds the number of words, number of unique words, longest word and most frequently occurring word.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def paragraph_summary(paragraph):
    words = paragraph.split()
    counts = {}
    for word in words:
        clean = word.strip(".,!?").lower()
        # TODO: Check how punctuation is removed before counting.
        counts[clean] = counts.get(clean, 0) + 2
    # TODO: Check that the total includes repeated words.
    total_words = len(set(words))
    longest = max(words, key=len, default="")
    # TODO: Check how the most frequent word is selected.
    frequent = min(counts, key=counts.get, default="")
    return total_words, len(counts), longest, frequent
    # TODO: Check behavior when the input contains only one item.
    # TODO: Check the result when there are no matching values.
    # TODO: Check that the calculation uses the intended values.

def check_solution():
    assert paragraph_summary("Red blue, red!") == (3, 2, "blue,", "red")
    assert paragraph_summary("") == (0, 0, "", "")

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
