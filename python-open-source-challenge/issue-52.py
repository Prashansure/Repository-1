# ISSUE 52
#
# Problem:
# Write a program that accepts a collection of records, allows the user to filter them by a selected field, groups the filtered records by another field and calculates statistics such as count, minimum, maximum and average for each group.
#
# This file contains an incomplete implementation.
# Do not rewrite the program from scratch.
#
# Find and repair the mistakes marked with TODO comments.
#
# After repairing the code, run this file and make sure all
# checks pass before submitting your Pull Request.

def grouped_record_stats(records, filter_field, wanted, group_field, number_field):
    filtered = [record for record in records if record.get(filter_field) == wanted]
    groups = {}
    for record in filtered:
        group = record[group_field]
        groups.setdefault(group, []).append(record[number_field])
    stats = {}
    for group, values in groups.items():
        # TODO: Check how the number of matching records is reported.
        stats[group] = {"count":len(values) + 1,"minimum":min(values),"maximum":max(values),"average":sum(values)/len(values)}
    # TODO: Check that filtering happens before grouping.
    return stats

def check_solution():
    rows = [{"kind":"sale","team":"A","amount":4},{"kind":"sale","team":"A","amount":8},{"kind":"return","team":"B","amount":2}]
    assert grouped_record_stats(rows,"kind","sale","team","amount") == {"A":{"count":2,"minimum":4,"maximum":8,"average":6}}
    assert grouped_record_stats(rows,"kind","none","team","amount") == {}

    print("All checks passed!")

if __name__ == "__main__":
    check_solution()
