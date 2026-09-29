# ISSUE 53
#
# Problem:
# Write a program that accepts transaction records containing date, category, type and amount and generates totals grouped by transaction type and category.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def transaction_totals(transactions):
    totals = {}
    for transaction in transactions:
        key = (transaction["type"], transaction["category"])
        # TODO: Check how each transaction amount affects its group.
        totals[key] = totals.get(key, 0) - transaction["amount"]
    # TODO: Check that type and category both distinguish totals.
    return totals

def check_solution():
    rows = [{"date":"Mon","category":"food","type":"debit","amount":12},{"date":"Tue","category":"food","type":"credit","amount":5},{"date":"Wed","category":"food","type":"debit","amount":3}]
    assert transaction_totals(rows) == {("debit","food"):15,("credit","food"):5}
    assert transaction_totals([]) == {}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
