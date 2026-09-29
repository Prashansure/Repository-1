# ISSUE 25
#
# Problem:
# Write a program that accepts monthly expense records and finds the month with the highest total spending and the category responsible for the highest spending.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def spending_summary(expenses):
    months = {}
    categories = {}
    for expense in expenses:
        month, category, amount = expense["month"], expense["category"], expense["amount"]
        # TODO: Check how monthly spending is accumulated.
        months[month] = months.get(month, 0) - amount
        by_month = categories.setdefault(month, {})
        by_month[category] = by_month.get(category, 0) + amount
    # TODO: Check the month selected from the totals.
    busiest = max(months, key=months.get, default="")
    # TODO: Check how the top category is chosen for that month.
    category = max(categories.get(busiest, {}), key=categories[busiest].get, default="")
    return busiest, category, months

def check_solution():
    rows = [{"month":"Jan","category":"food","amount":20},{"month":"Jan","category":"travel","amount":10},{"month":"Feb","category":"food","amount":50}]
    month, category, totals = spending_summary(rows)
    assert month == "Feb" and category == "food" and totals == {"Jan":30,"Feb":50}
    assert spending_summary([])[:2] == ("", "")

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
