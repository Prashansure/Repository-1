# ISSUE 66
#
# Problem:
# Write a program that accepts hotel booking records containing room type, number of nights and price per night and calculates total revenue and occupancy for every room type.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def room_type_report(bookings):
    report = {}
    for booking in bookings:
        kind = booking["room_type"]
        room = report.setdefault(kind, {"revenue":0,"nights":0})
        # TODO: Check how price per night contributes to revenue.
        room["revenue"] += booking["price_per_night"]
        # TODO: Check how the booked nights affect occupancy.
        room["nights"] += booking["nights"] + 1
    # TODO: Check that all room types appear in the report.
    return report

def check_solution():
    bookings = [{"room_type":"single","nights":2,"price_per_night":50},{"room_type":"single","nights":1,"price_per_night":50},{"room_type":"suite","nights":3,"price_per_night":100}]
    assert room_type_report(bookings) == {"single":{"revenue":150,"nights":3},"suite":{"revenue":300,"nights":3}}
    assert room_type_report([]) == {}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
