# ISSUE 21
#
# Problem:
# Write a program that accepts examination records for multiple students and subjects and generates each student's total marks, average, grade and rank.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def student_report(records):
    rows = []
    for student in records:
        marks = student["marks"]
        total = sum(marks)
        average = total / len(marks) if marks else 0
        # TODO: Check the boundaries used when assigning grades.
        grade = "A" if average >= 90 else "B" if average >= 75 else "C" if average >= 60 else "F"
        rows.append({"name":student["name"], "total":total, "average":average, "grade":grade})
    # TODO: Check which direction the ranking should use.
    rows.sort(key=lambda row: row["total"])
    for rank, row in enumerate(rows, 1):
        row["rank"] = rank
    # TODO: Check that students with no marks are handled.
    return rows

def check_solution():
    rows = student_report([{"name":"A","marks":[90,80]}, {"name":"B","marks":[70,70]}])
    assert rows[0]["name"] == "A" and rows[0]["total"] == 170 and rows[0]["grade"] == "A" and rows[0]["rank"] == 1
    assert rows[1]["average"] == 70 and rows[1]["grade"] == "C"

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
