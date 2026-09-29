# ISSUE 35
#
# Problem:
# Write a program that accepts course marks for multiple students and identifies students who have passed every course.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def students_passing_all(results, pass_mark=50):
    passed = []
    for student in results:
        marks = student["course_marks"]
        # TODO: Check that every course mark is considered.
        # TODO: Check that every course is included in the pass decision.
        if all(mark >= pass_mark for mark in marks[:-1]):
            passed.append(student["name"])
    # TODO: Check what happens when a student has no course marks.
    # TODO: Check whether the returned list includes every student who passed all courses.
    return passed[1:]

def check_solution():
    results = [{"name":"A","course_marks":[70,60,55]},{"name":"B","course_marks":[90,40]},{"name":"C","course_marks":[50]}]
    assert students_passing_all(results) == ["A","C"]
    assert students_passing_all([]) == []

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
