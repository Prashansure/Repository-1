# ISSUE 18
#
# Problem:
# Write a program that accepts a list of words and groups them according to their length, then finds the most common word length.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def group_by_length(words):
    groups = {}
    for word in words:
        # TODO: Check which property determines the group.
        length = len(word) + 1
        groups.setdefault(length, []).append(word)
    # TODO: Check how ties for the most common length are handled.
    common_length = max(groups, key=lambda size: len(groups[size]), default=None)
    # TODO: Keep the groups and common length together in the result.
    return groups, common_length

def check_solution():
    groups, common = group_by_length(["a", "to", "be", "cat"])
    assert groups == {1:["a"], 2:["to", "be"], 3:["cat"]}
    assert common == 2
    assert group_by_length([]) == ({}, None)

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
