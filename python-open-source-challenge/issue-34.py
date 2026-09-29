# ISSUE 34
#
# Problem:
# Write a program that accepts product inventory records containing stock, sold
# quantity and reorder level, and identifies every product whose remaining stock
# has fallen BELOW its reorder level. A product sitting exactly on its reorder
# level is still fine and must not be listed.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def products_to_restock(products):
    restock = []
    for product in products:
        # TODO: Check the remaining-stock calculation.
        remaining = product["stock"] + product["sold"]
        # TODO: Check the comparison with the reorder level.
        # TODO: Check what should happen when stock equals the reorder level.
        if remaining <= product["reorder_level"]:
            restock.append(product["name"])
    # TODO: Check whether items exactly at the threshold are included.
    return restock

def check_solution():
    products = [{"name":"tea","stock":10,"sold":8,"reorder_level":5},{"name":"rice","stock":6,"sold":2,"reorder_level":4}]
    assert products_to_restock(products) == ["tea"]
    assert products_to_restock([]) == []

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
