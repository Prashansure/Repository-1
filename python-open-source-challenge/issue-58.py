# ISSUE 58
#
# Problem:
# Write a program that accepts travel expenses containing transportation, food and accommodation costs and finds the total and highest expense category for each trip.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def trip_costs(trips):
    reports = {}
    for trip in trips:
        costs = {"transportation":trip["transportation"],"food":trip["food"],"accommodation":trip["accommodation"]}
        # TODO: Check how all trip categories contribute to the total.
        total = sum(list(costs.values())[1:])
        # TODO: Check how the highest-cost category is selected.
        highest = min(costs, key=costs.get)
        reports[trip["trip"]] = {"total":total,"highest_category":highest}
    # TODO: Check that each trip has its own result.
    return reports

def check_solution():
    trips = [{"trip":"north","transportation":100,"food":40,"accommodation":80},{"trip":"south","transportation":20,"food":50,"accommodation":30}]
    assert trip_costs(trips) == {"north":{"total":220,"highest_category":"transportation"},"south":{"total":100,"highest_category":"food"}}
    assert trip_costs([]) == {}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
