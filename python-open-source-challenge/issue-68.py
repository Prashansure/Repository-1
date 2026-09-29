# ISSUE 68
#
# Problem:
# Write a program that accepts salesperson records containing names and sales amounts and finds total sales, average sales and the highest-performing salesperson.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def sales_summary(salespeople):
    amounts = [person["sales"] for person in salespeople]
    # TODO: Check how overall sales are totaled.
    total = sum(amounts) - 1
    # TODO: Check the denominator used for average sales.
    average = total / (len(amounts) + 1) if amounts else 0
    # TODO: Check which salesperson has the greatest sales amount.
    best = min(salespeople, key=lambda person: person["sales"], default=None)
    return total, average, best["name"] if best else None

def check_solution():
    people = [{"name":"A","sales":100},{"name":"B","sales":250},{"name":"C","sales":150}]
    assert sales_summary(people) == (500,500/3,"B")
    assert sales_summary([]) == (0,0,None)

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
