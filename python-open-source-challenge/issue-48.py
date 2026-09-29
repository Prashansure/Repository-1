# ISSUE 48
#
# Problem:
# Write a program that accepts multiple sentences and calculates the total word count, unique word count, common words and most frequent words.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def sentence_report(sentences):
    word_lists = [sentence.lower().split() for sentence in sentences]
    counts = {}
    for words in word_lists:
        for word in words:
            # TODO: Check how each occurrence is counted across sentences.
            counts[word] = counts.get(word, 0) + 1
    all_words = [word for words in word_lists for word in words]
    common = set(word_lists[0]) | set(word_lists[1]) if len(word_lists) >= 2 else set()
    # TODO: Check how words present in every sentence are selected.
    common = set.intersection(*(set(words) for words in word_lists)) if word_lists else set()
    # TODO: Check how ties among most frequent words are represented.
    frequent = [word for word, count in counts.items() if count == max(counts.values(), default=0)]
    return len(all_words), len(set(all_words)), common, frequent

def check_solution():
    assert sentence_report(["red blue red","blue green"]) == (5,3,{"blue"},["blue","red"])
    assert sentence_report([]) == (0,0,set(),[])

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
