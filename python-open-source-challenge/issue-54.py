# ISSUE 54
#
# Problem:
# Write a program that accepts student marks from two examinations and generates a report showing each student's improvement percentage and performance category.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def exam_report(students):
    report = []
    for student in students:
        first, second = student["exam1"], student["exam2"]
        # TODO: Check which exam score is the percentage baseline.
        change = (second - first) / second * 100 if second else 0
        # TODO: Check how direction of change maps to a category.
        category = "improved" if change < 0 else "declined" if change > 0 else "unchanged"
        report.append({"name":student["name"],"improvement":change,"category":category})
    # TODO: Check that each student's report is retained.
    return report

def check_solution():
    students = [{"name":"A","exam1":50,"exam2":75},{"name":"B","exam1":80,"exam2":60},{"name":"C","exam1":70,"exam2":70}]
    result = exam_report(students)
    assert result[0] == {"name":"A","improvement":50,"category":"improved"}
    assert result[1]["category"] == "declined" and result[2]["category"] == "unchanged"

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
