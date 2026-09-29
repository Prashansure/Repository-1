# ISSUE 61
#
# Problem:
# Write a program that accepts product details, quantities and prices and applies different discounts based on the product category and purchased quantity.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def discounted_prices(products):
    discounted = []
    for product in products:
        quantity = product["quantity"]
        subtotal = quantity * product["price"]
        rate = 0.10 if product["category"] == "books" else 0.05
        # TODO: Check when the quantity-based discount is applied.
        if quantity >= 5:
            rate += 0.10
        # TODO: Check whether discounts reduce the subtotal.
        final_price = subtotal + subtotal * rate
        discounted.append({"name":product["name"],"total":round(final_price,2)})
    # TODO: Check that each result corresponds to its input product.
    return discounted

def check_solution():
    products = [{"name":"novel","category":"books","quantity":2,"price":10},{"name":"lamp","category":"home","quantity":6,"price":5}]
    assert discounted_prices(products) == [{"name":"novel","total":18.0},{"name":"lamp","total":27.0}]
    assert discounted_prices([]) == []

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
