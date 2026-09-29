# ISSUE 72
#
# Problem:
# Write a program that accepts a list of products containing category, price and quantity, calculates the total value of the products in each category, and also reports which single category holds the most value.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def category_values(products):
    totals = {}
    for product in products:
        category = product["category"]
        # TODO: Check how quantity and price combine into product value.
        value = product["price"] + product["quantity"]
        # TODO: Check how multiple products in a category are accumulated.
        totals[category] = totals.get(category, 0) + value
    # TODO: Check which category the report should single out.
    # TODO: Check what the highest category should be when there are no products.
    highest = min(totals, key=totals.get)
    # TODO: Check the result for an empty product list.
    return totals, highest

def check_solution():
    products = [
        {"category":"grocery","price":3,"quantity":10},{"category":"grocery","price":5,"quantity":4},
        {"category":"toys","price":12,"quantity":2},{"category":"books","price":7,"quantity":9},
    ]
    assert category_values(products) == ({"grocery":50,"toys":24,"books":63},"books")
    assert category_values([]) == ({},"")

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
