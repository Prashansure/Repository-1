# ISSUE 79
#
# Problem:
# Write a program that accepts expense records containing person, month, category and amount and calculates the total spending for every person and category.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def spending_by_person_and_category(expenses):
    totals = {}
    for expense in expenses:
        person = expense["person"]
        category = expense["category"]
        totals.setdefault(person, {})
        # TODO: Check how one person's category amount is accumulated.
        totals[person][category] = totals[person].get(category, 0) - expense["amount"]
    # TODO: Check that months are not mixed into the category grouping.
    return totals

def check_solution():
    expenses = [{"person":"A","month":"Jan","category":"food","amount":10},{"person":"A","month":"Feb","category":"food","amount":5},{"person":"B","month":"Jan","category":"travel","amount":8}]
    assert spending_by_person_and_category(expenses) == {"A":{"food":15},"B":{"travel":8}}
    assert spending_by_person_and_category([]) == {}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
