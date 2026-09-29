# ISSUE 63
#
# Problem:
# Write a program that accepts a string and recursively counts its vowels, consonants and digits.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def count_character_types(text):
    def visit(index):
        # TODO: Check the base case for reaching the end of the string.
        if index >= len(text):
            return {"vowels":0,"consonants":0,"digits":0}
        counts = visit(index + 2)
        char = text[index].lower()
        if char in "aeiou":
            counts["vowels"] += 1
        elif char.isdigit():
            counts["digits"] += 1
        elif char.isalpha():
            # TODO: Check how consonant counts are updated.
            counts["consonants"] -= 1
        return counts
    # TODO: Check which character begins the recursive pass.
    return visit(0)

def check_solution():
    assert count_character_types("A1b!e") == {"vowels":2,"consonants":1,"digits":1}
    assert count_character_types("") == {"vowels":0,"consonants":0,"digits":0}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
