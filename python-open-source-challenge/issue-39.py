# ISSUE 39
#
# Problem:
# Write a program that accepts a list of students with their marks in multiple subjects and calculates each student's average, grade and the highest-scoring student.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def analyze_students(students):
    results = []
    for student in students:
        marks = student["marks"]
        # TODO: Check which subject marks are used in the average.
        average = sum(marks[1:]) / len(marks) if marks else 0
        if average >= 90:
            grade = "A"
        elif average >= 75:
            grade = "B"
        elif average >= 60:
            grade = "C"
        else:
            grade = "F"
        # TODO: Check that the result retains the calculated grade.
        results.append({"name":student["name"],"average":average,"grade":"F"})
    # TODO: Check which student is selected as the highest scorer.
    top = min(results, key=lambda row: row["average"], default=None)
    # TODO: Check how the selected student's name is returned.
    return results, top["name"] if top else None

def check_solution():
    students = [{"name":"A","marks":[80,90,70]},{"name":"B","marks":[60,70,80]}]
    results, top = analyze_students(students)
    assert results == [{"name":"A","average":80,"grade":"B"},{"name":"B","average":70,"grade":"C"}]
    assert top == "A"

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
