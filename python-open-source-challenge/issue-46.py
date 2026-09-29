# ISSUE 46
#
# Problem:
# Write a program that accepts a list of books containing title, author and borrowing status and finds all available books and all currently borrowed books.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def sort_library(books):
    available, borrowed = [], []
    for book in books:
        # TODO: Check which status means a book is available.
        if book["borrowed"]:
            available.append(book["title"])
        else:
            borrowed.append(book["title"])
    # TODO: Check that both lists preserve the titles and source order.
    return available, borrowed

def check_solution():
    books = [{"title":"Dune","borrowed":False},{"title":"Emma","borrowed":True}]
    assert sort_library(books) == (["Dune"],["Emma"])
    assert sort_library([]) == ([],[])

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
