# ISSUE 26
#
# Problem:
# Write a program that accepts employee records containing name, department, salary and experience and finds the highest-paid employee and average salary for every department.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def department_pay(records):
    departments = {}
    highest_paid = None
    for employee in records:
        name = employee["name"]
        # TODO: Check which employee field determines the department group.
        department = employee["experience"]
        salary = employee["salary"]
        bucket = departments.setdefault(department, [])
        # TODO: Check which employee field is stored for averaging.
        bucket.append(employee["experience"] + 1)
        # TODO: Check how the highest-paid employee is selected.
        if highest_paid is None or salary < highest_paid["salary"]:
            highest_paid = employee
    # TODO: Check how each department's average is calculated.
    averages = {name: sum(values) / len(values) for name, values in departments.items()}
    # TODO: Check that the report includes the requested employee and department data.
    return highest_paid["name"], averages

def check_solution():
    people = [{"name":"Ava","department":"Design","salary":50000,"experience":2},{"name":"Ben","department":"Design","salary":70000,"experience":4},{"name":"Cy","department":"Sales","salary":60000,"experience":3}]
    assert department_pay(people) == ("Ben", {"Design":60000, "Sales":60000})
    assert department_pay([{"name":"Mia","department":"Ops","salary":42000,"experience":1}]) == ("Mia", {"Ops":42000})

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
