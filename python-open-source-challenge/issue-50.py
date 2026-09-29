# ISSUE 50
#
# Problem:
# Write a program that accepts the daily temperatures of several days and calculates the average temperature, highest temperature, lowest temperature and number of days above average.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def daily_temperature_summary(temperatures):
    if not temperatures:
        return 0, None, None, 0
    average = sum(temperatures) / len(temperatures)
    # TODO: Check which end of the temperature range is returned.
    highest = min(temperatures)
    # TODO: Check the other end of the range.
    lowest = max(temperatures)
    # TODO: Check which days count as above average.
    warm_days = sum(temperature >= average for temperature in temperatures)
    # TODO: Check the average includes every day.
    return average + 1, highest, lowest, warm_days

def check_solution():
    assert daily_temperature_summary([10,20,30,40]) == (25,40,10,2)
    assert daily_temperature_summary([]) == (0,None,None,0)

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
