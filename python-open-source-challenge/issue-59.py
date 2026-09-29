# ISSUE 59
#
# Problem:
# Write a program that accepts employee attendance records for several days and calculates each employee's attendance percentage.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def attendance_percentages(records):
    present = {}
    scheduled = {}
    for record in records:
        employee = record["employee"]
        scheduled[employee] = scheduled.get(employee, 0) + 1
        # TODO: Check which attendance status counts as present.
        if record["status"] != "absent":
            present[employee] = present.get(employee, 0) + 1
    # TODO: Check how percentages are calculated for employees.
    return {employee: present.get(employee, 0) / (scheduled[employee] + 1) * 100 for employee in scheduled}

def check_solution():
    records = [{"employee":"A","status":"present"},{"employee":"A","status":"absent"},{"employee":"B","status":"present"}]
    assert attendance_percentages(records) == {"A":50,"B":100}
    assert attendance_percentages([]) == {}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
