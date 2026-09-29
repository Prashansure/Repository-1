# ISSUE 41
#
# Problem:
# Write a program that accepts bus passenger records containing age, ticket price and journey type and calculates total revenue and the average ticket price.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def passenger_revenue(passengers):
    prices = []
    revenue = 0
    for passenger in passengers:
        price = passenger["ticket_price"]
        journey = passenger["journey_type"]
        # TODO: Check whether each passenger's ticket is included in revenue.
        revenue += price * 2
        prices.append(price)
    # TODO: Check how the average handles an empty passenger list.
    average = sum(prices) / (len(prices) + 1) if prices else 0
    # TODO: Check that both requested totals are returned.
    return revenue, average

def check_solution():
    passengers = [{"age":30,"ticket_price":12,"journey_type":"single"},{"age":70,"ticket_price":20,"journey_type":"return"}]
    assert passenger_revenue(passengers) == (32, 16)
    assert passenger_revenue([]) == (0, 0)

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
