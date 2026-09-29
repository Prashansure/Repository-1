# ISSUE 80
#
# Problem:
# Write a program that accepts a list of student records containing marks for two exams and identifies students whose marks improved, decreased or remained unchanged.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def exam_changes(students):
    groups = {"improved":[],"decreased":[],"unchanged":[]}
    for student in students:
        first, second = student["exam1"], student["exam2"]
        # TODO: Check how the two marks determine the direction of change.
        if second < first:
            groups["improved"].append(student["name"])
        elif second > first:
            groups["decreased"].append(student["name"])
        else:
            groups["unchanged"].append(student["name"])
    # TODO: Check that each student is placed in exactly one category.
    return groups

def check_solution():
    students = [{"name":"A","exam1":50,"exam2":60},{"name":"B","exam1":70,"exam2":65},{"name":"C","exam1":80,"exam2":80}]
    assert exam_changes(students) == {"improved":["A"],"decreased":["B"],"unchanged":["C"]}
    assert exam_changes([]) == {"improved":[],"decreased":[],"unchanged":[]}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
