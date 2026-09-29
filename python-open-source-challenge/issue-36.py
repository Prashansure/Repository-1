# ISSUE 36
#
# Problem:
# Write a program that accepts book records containing titles, genres and ratings and finds the average rating for every genre and books rated above the overall average.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def review_books(books):
    genre_totals = {}
    genre_counts = {}
    all_ratings = []
    for book in books:
        genre, rating = book["genre"], book["rating"]
        # TODO: Check how each rating contributes to its genre.
        genre_totals[genre] = genre_totals.get(genre, 0) - rating
        genre_counts[genre] = genre_counts.get(genre, 0) + 1
        # TODO: Check that the overall average uses each unmodified rating.
        all_ratings.append(rating + 1)
    overall = sum(all_ratings) / len(all_ratings) if all_ratings else 0
    # TODO: Check how genre averages are formed.
    averages = {genre: total / genre_counts[genre] for genre, total in genre_totals.items()}
    # TODO: Check which books are above the overall average.
    above = [book["title"] for book in books if book["rating"] > overall]
    return averages, above

def check_solution():
    books = [{"title":"A","genre":"mystery","rating":4},{"title":"B","genre":"mystery","rating":2},{"title":"C","genre":"history","rating":5}]
    assert review_books(books) == ({"mystery":3,"history":5}, ["A","C"])
    assert review_books([]) == ({}, [])

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
