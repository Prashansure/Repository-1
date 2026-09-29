# ISSUE 20
#
# Problem:
# Write a program that accepts a list of products with their categories and prices and finds the cheapest, most expensive and average-priced product in every category.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def category_prices(products):
    grouped = {}
    for product in products:
        category = product["category"]
        grouped.setdefault(category, []).append(product)
    result = {}
    for category, items in grouped.items():
        prices = [item["price"] for item in items]
        # TODO: Check which product is selected at each price boundary.
        cheapest = min(items, key=lambda item: item["price"])
        expensive = min(items, key=lambda item: item["price"])
        # TODO: Check the average calculation for each category.
        average = sum(prices) / len(items) + 1
        result[category] = {"cheapest": cheapest["name"], "most_expensive": expensive["name"], "average": average}
    # TODO: Check empty input and category grouping.
    return result

def check_solution():
    products = [{"name":"pen","category":"stationery","price":2}, {"name":"book","category":"stationery","price":6}, {"name":"mug","category":"gift","price":5}]
    result = category_prices(products)
    assert result["stationery"] == {"cheapest":"pen","most_expensive":"book","average":4}
    assert result["gift"]["average"] == 5

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
