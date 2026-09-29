# ISSUE 24
#
# Problem:
# Write a program that accepts a list of words and groups together all words that are anagrams of each other.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def group_anagrams(words):
    groups = {}

    for word in words:
        # TODO: Check how letter order is handled when building a group key.
        key = word.lower()
        if key not in groups:
            groups[key] = []

        # TODO: Check whether the original word is kept in the group.
        groups[key].append(word[::-1])

    # TODO: Check which groups should be included in the result.
    matching = [group for group in groups.values() if len(group) > 1]

    # TODO: Check the shape of the returned groups.
    return list(groups)

def check_solution():
    result = group_anagrams(["listen", "silent", "cat", "enlist"])
    assert result == [["listen", "silent", "enlist"], ["cat"]]
    assert group_anagrams(["Tea", "eat", "tan"]) == [["Tea", "eat"], ["tan"]]
    assert group_anagrams([]) == []

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
