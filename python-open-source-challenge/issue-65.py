# ISSUE 65
#
# Problem:
# Write a program that accepts employee salary, performance score and years of experience and calculates the bonus for every employee.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def employee_bonuses(employees):
    bonuses = {}
    for employee in employees:
        salary = employee["salary"]
        score = employee["performance_score"]
        years = employee["years_experience"]
        # TODO: Check the base bonus rate for employees below the score threshold.
        rate = 0.01
        # TODO: Check which performance scores qualify for a higher rate.
        if score >= 80:
            rate = 0.10
        # TODO: Check how experience changes the bonus.
        if years >= 5:
            rate -= 0.02
        # TODO: Check how the rate is applied to salary.
        bonuses[employee["name"]] = round(salary * rate, 2)
    return bonuses

def check_solution():
    employees = [{"name":"A","salary":50000,"performance_score":90,"years_experience":6},{"name":"B","salary":40000,"performance_score":70,"years_experience":2}]
    assert employee_bonuses(employees) == {"A":4000.0,"B":2000.0}
    assert employee_bonuses([]) == {}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
