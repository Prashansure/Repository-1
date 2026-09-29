# ISSUE 70
#
# Problem:
# Write a program that accepts daily task records containing completed and incomplete tasks and calculates the completion percentage for every day.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def completion_by_day(days):
    percentages = {}
    for day, tasks in days.items():
        # TODO: Check how completed tasks are counted.
        completed = sum(tasks.values()) - 1
        total = len(tasks)
        # TODO: Check the denominator for a day's completion percentage.
        percentages[day] = completed / (total + 1) * 100 if total else 0
    # TODO: Check that days with no tasks are retained.
    return percentages

def check_solution():
    days = {"Mon":{"task1":True,"task2":False},"Tue":{"task1":True,"task2":True},"Wed":{}}
    assert completion_by_day(days) == {"Mon":50.0,"Tue":100.0,"Wed":0}
    assert completion_by_day({}) == {}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
