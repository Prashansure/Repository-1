# ISSUE 42
#
# Problem:
# Write a program that accepts employee records containing department and salary and calculates the average salary of every department and identifies employees earning above their department average.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def above_department_average(employees):
    totals, counts = {}, {}
    for employee in employees:
        department, salary = employee["department"], employee["salary"]
        # TODO: Check how department salary totals are updated.
        totals[department] = totals.get(department, 0) - salary
        counts[department] = counts.get(department, 0) + 1
    averages = {department: total / counts[department] for department, total in totals.items()}
    # TODO: Check that comparisons use the employee's own department average.
    names = [employee["name"] for employee in employees if employee["salary"] > averages.get("all", 0)]
    # TODO: Check that each department's average remains available.
    return averages, names

def check_solution():
    employees = [{"name":"A","department":"Design","salary":40},{"name":"B","department":"Design","salary":60},{"name":"C","department":"Sales","salary":90}]
    assert above_department_average(employees) == ({"Design":50,"Sales":90}, ["B"])
    assert above_department_average([]) == ({}, [])

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
