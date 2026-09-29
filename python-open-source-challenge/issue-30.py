# ISSUE 30
#
# Problem:
# Write a program that accepts monthly electricity consumption values and calculates the electricity bill using different consumption slabs.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def electricity_bill(units_by_month):
    bills = []
    for units in units_by_month:
        # TODO: Check how the first usage slab is charged.
        bill = min(units, 100) * 1.0
        if units > 100:
            # TODO: Check where the second slab begins and ends.
            bill += min(units - 100, 100) * 1.5
        if units > 200:
            # TODO: Check the rate applied to usage above the second slab.
            bill += (units - 200) * 3.0
        # TODO: Check how negative or zero usage is handled.
        bills.append(round(bill, 2))
    # TODO: Check that monthly bills stay in input order.
    return bills

def check_solution():
    assert electricity_bill([50, 150, 250]) == [50.0, 200.0, 450.0]
    assert electricity_bill([0]) == [0.0]

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
