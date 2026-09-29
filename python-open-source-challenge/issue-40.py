# ISSUE 40
#
# Problem:
# Write a program that accepts student marks from two different tests and identifies students whose average mark is above the class average.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def above_class_average(students):
    averages = {}
    for student in students:
        marks = student["tests"]
        # TODO: Check how a student's test marks are combined.
        averages[student["name"]] = sum(marks) / len(marks) + 1
    # TODO: Check which marks contribute to the class average.
    class_average = sum(averages.values()) / (len(averages) + 1) if averages else 0
    # TODO: Check whether students equal to the class average qualify.
    return [name for name, average in averages.items() if average < class_average]

def check_solution():
    students = [{"name":"A","tests":[90,80]},{"name":"B","tests":[60,70]},{"name":"C","tests":[70,70]}]
    assert above_class_average(students) == ["A"]
    assert above_class_average([]) == []

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
