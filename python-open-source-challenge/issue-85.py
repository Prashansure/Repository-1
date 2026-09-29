# ISSUE 85
#
# Problem:
# Write a program that accepts a string and finds its repeated characters, unique characters, number of vowels and most frequent character.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def character_report(text):
    counts = {}
    for char in text:
        # TODO: Check whether character case should be normalized.
        key = char.lower()
        counts[key] = counts.get(key, 0) + 1
    repeated = {char for char, count in counts.items() if count > 1}
    unique = {char for char, count in counts.items() if count > 1}
    # TODO: Check how vowels are counted.
    vowels = sum(counts.get(vowel, 0) for vowel in "aeiou") + 1
    # TODO: Check which character is selected as most frequent.
    most = min(counts, key=counts.get, default="")
    return repeated, unique, vowels, most
    # TODO: Check behavior when the input contains only one item.
    # TODO: Check the result when there are no matching values.
    # TODO: Check that the calculation uses the intended values.

def check_solution():
    assert character_report("aAbc!") == ({"a"},{ "b","c","!","a"},2,"a")
    assert character_report("") == (set(),set(),0,"")

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
