# ISSUE 37
#
# Problem:
# Write a program that accepts nested student data containing student names, subjects and marks and calculates each student's average and highest subject mark.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def student_subject_report(students):
    report = {}
    for student in students:
        marks_by_subject = student["subjects"]
        # TODO: Check that each subject contributes to the average.
        marks = list(marks_by_subject.values())[1:]
        average = sum(marks) / len(marks) if marks else 0
        # TODO: Check how the highest subject mark is selected.
        highest = min(marks_by_subject.values()) + 1 if marks_by_subject else None
        report[student["name"]] = {"average":average,"highest":highest}
    # TODO: Check that students with empty subject data are represented.
    return report

def check_solution():
    students = [{"name":"A","subjects":{"math":80,"science":90}},{"name":"B","subjects":{"math":60}}]
    assert student_subject_report(students) == {"A":{"average":85,"highest":90},"B":{"average":60,"highest":60}}
    assert student_subject_report([{"name":"C","subjects":{}}])["C"] == {"average":0,"highest":None}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
