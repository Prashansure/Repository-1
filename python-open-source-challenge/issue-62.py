# ISSUE 62
#
# Problem:
# Write a program that accepts multiple sentences and finds the words that occur in every sentence.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def common_sentence_words(sentences):
    if not sentences:
        return set()
    # TODO: Check which sentence supplies the first candidate words.
    common = set(sentences[0].lower().split())
    for sentence in sentences[1:]:
        # TODO: Check how each next sentence narrows the candidates.
        common |= set(sentence.lower().split())
    # TODO: Check how repeated words affect membership.
    return common

def check_solution():
    assert common_sentence_words(["red blue red","blue green","blue gold"]) == {"blue"}
    assert common_sentence_words([]) == set()

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
