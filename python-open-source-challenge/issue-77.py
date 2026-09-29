# ISSUE 77
#
# Problem:
# Write a program that accepts a list of student records and calculates the total marks, average marks and rank of every student.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def student_ranks(students):
    results = []
    for student in students:
        marks = student["marks"]
        # TODO: Check that every mark contributes to the total.
        total = sum(marks[1:])
        average = total / len(marks) if marks else 0
        results.append({"name":student["name"],"total":total,"average":average})
    # TODO: Check the direction used to order student ranks.
    results.sort(key=lambda row: row["total"])
    for rank, result in enumerate(results, 1):
        result["rank"] = rank
    # TODO: Check how students with no marks are represented.
    return results

def check_solution():
    result = student_ranks([{"name":"A","marks":[80,90]},{"name":"B","marks":[60,70]}])
    assert result == [{"name":"A","total":170,"average":85,"rank":1},{"name":"B","total":130,"average":65,"rank":2}]
    assert student_ranks([]) == []

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
