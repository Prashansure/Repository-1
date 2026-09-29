# ISSUE 81
#
# Problem:
# Write a program that accepts product records containing the starting stock and the quantity sold, works out how many units of each product are left, and identifies any product that has been oversold — one where more units were sold than were ever in stock.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def stock_report(products):
    remaining = {}
    oversold = []
    for product in products:
        # TODO: Check how units sold change the stock that is left.
        left = product["stock"] + product["sold"]
        remaining[product["name"]] = left
        # TODO: Check the condition that means a product was oversold.
        # TODO: Check what should happen when a product sold its entire stock.
        if left <= 0:
            oversold.append(product["name"])
    # TODO: Check that both results are returned together.
    return remaining, oversold

def check_solution():
    products = [{"name":"tea","stock":10,"sold":8},{"name":"rice","stock":6,"sold":9},{"name":"salt","stock":4,"sold":4}]
    assert stock_report(products) == ({"tea":2,"rice":-3,"salt":0},["rice"])
    assert stock_report([]) == ({},[])

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
